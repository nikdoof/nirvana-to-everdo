# NirvanaHQ to EverDo

A simple script to convert a NirvanaHQ JSOn export into the Everdo JSON format.

## Requirements

This script has been tested on Python 3.8.3, included in the current version of Windows 10. The script should support any version of Python from v2.7 onwards due to the limited use of Py3 features.

## Usage

Run ```nirvana-to-everdo.py``` with your Nirvana JSON export, and pipe the output to a a filename you want

```
$ nirvana-to-everdo.py nirvana.json > everdo.json
```

When completed, import the resulting file with Everdo's import function.