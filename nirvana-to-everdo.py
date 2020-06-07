#!/usr/env python
import sys
import json
import uuid
import datetime
import time

with open(sys.argv[1], 'r') as fobj:
    data = json.load(fobj)

items = []
tags = []

def get_or_create_tag(tag_name):
    for tag in tags:
        if tag_name == tag['title']:
            return tag['id']
    tag_id = str(uuid.uuid4())
    tags.append({
        'id': tag_id,
        'title': tag_name,
        'type': 'l',
    })
    return tag_id

for item in data:
    result = {
        'id': item['id'].replace('-', ''),
        'title': item['name'],
        'created_on': int(item['created']),\
        'note': item['note'],
        'tags': [],
    }

    # Set type
    TYPE_LOOKUP = {
        '0': 'a',
        '1': 'p',
        '2': 'n',
        '3': 'l',
    }
    result['type'] = TYPE_LOOKUP[item['type']]

    # State
    STATE_LOOKUP = {
        '0': 'a',
        '1': 'a',
        '4': 'm',
        '6': 'd',
        '7': 'r',
        '9': 's',
        '10': 'a',
        '11': 'a',
    }
    result['list'] = STATE_LOOKUP[item['state']]

    # Completed
    if int(item['completed']) > 0:
        result['completed_on'] = int(item['completed'])

    # Parent ID
    if item['parentid'] != '':
        result['parent_id'] = item['parentid'].replace('-', '')

    # Due Date
    if item['duedate'] and int(item['duedate']) > 0:
        result['due_date'] = int(time.mktime(datetime.datetime.strptime(item['duedate'], '%Y%m%d').timetuple()))

    # Estimated Time
    if item['etime'] and int(item['etime']) > 0:
        result['time'] = int(item['etime'])

    # Set Energy
    if item['energy'] and int(item['energy']) > 0:
        result['energy'] = int(item['energy'])

    # Add tags
    item_tags = [x for x in item['tags'].split(',') if x != '']
    for item_tag in item_tags:
        result['tags'].append(get_or_create_tag(item_tag))

    items.append(result)

sys.stdout.write(json.dumps({
    'items': items,
    'tags': tags,
}))