import sys
import httplib
import urllib
from ConfigParser import SafeConfigParser

CONFIG = 'config.ini'

# TODO: Error checking would be glorious here
parser = SafeConfigParser()
parser.read(CONFIG)

#
# Build the alert message
#
#   Messages are currently limited to 1024 4-byte UTF-8 characters, with a title
#   of up to 250 characters. Supplementary URLs are limited to 512 characters,
#   and URL titles to 100 characters.

# TODO: Formatting sucks here
conn = httplib.HTTPSConnection("api.pushover.net:443")
conn.request("POST", "/1/messages.json",
               urllib.urlencode({
                       "token": parser.get('pushover', 'token'),
                       "user": parser.get('pushover', 'user'),
                       "message": sys.argv[5],
                     }), { "Content-type": "application/x-www-form-urlencoded" })
conn.getresponse()

# Splunk alert args

#for arg in sys.argv:
#    print arg

#   [
#   '/opt/splunk/pushover/bin/python',
#   '/opt/splunk/pushover/bin/scripts/pushover-splunk.py',
#   '345',
#   'index=_internal',
#   'index=_internal',
#   'test alert',
#   'Saved Search [test
#       alert] number of events(345)',
#   'http://mwalker-mbpr15.local:8000/app/search/search?q=%7Cloadjob%20scheduler__mike__search__RMD5354c629e1e04adb1_at_1437438600_1%20%7C%20head%20192%20%7C%20tail%201&earliest=0&latest=now',
#   '',
#   '/opt/splunk/pushover/var/run/splunk/dispatch/scheduler__mike__search__RMD5354c629e1e04adb1_at_1437438600_1/per_result_alert/tmp_191.csv.gz'
#   ]


