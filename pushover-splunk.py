import sys
import httplib
import urllib
from ConfigParser import SafeConfigParser

CONFIG = 'config.ini'

# TODO: Error checking would be glorious here
# TODO: Probably wont use ConfigParser anyway, should use splunk cred mgmt
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
conn.request(
    "POST",
    "/1/messages.json",
    urllib.urlencode(
        {
            "token": parser.get('pushover', 'token'),
            "user": parser.get('pushover', 'user'),
            "message": sys.argv[5],
        }
    ),
    {"Content-type": "application/x-www-form-urlencoded"}
)

conn.getresponse()

# Splunk alert args
#
# Arg EnvVar          Value
# 0   SPLUNK_ARG_0    Script name
# 1   SPLUNK_ARG_1    Number of events returned
# 2   SPLUNK_ARG_2    Search terms
# 3   SPLUNK_ARG_3    Fully qualified query string
# 4   SPLUNK_ARG_4    Name of report
# 5   SPLUNK_ARG_5    Trigger reason
#                     For example, "The number of events was greater than 1."
# 6   SPLUNK_ARG_6    Browser URL to view the report.
# 7   SPLUNK_ARG_7    Not used for historical reasons.
# 8   SPLUNK_ARG_8    File in which the results for the search are stored.
#                     Contains raw results.
