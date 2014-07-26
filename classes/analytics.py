"""
Basic analtics

The purpose of this file is to simply send a 'ping' with a unique identifier
and the script version once a day to give an indication of unique users

This has been added because Github doesn't show a download counter, I have no
way of knowing if this script is even being used (except for people telling me
it broke).

You are free to opt-out by disabling the config option

    analytics:
        enable:     True <- make this False

If the computer doesn't have internet access the script will continue as normal


Released under the MIT license
Copyright (c) 2012, Jason Millward

@category   misc
@version    $Id: 1.6, 2014-07-21 18:48:00 CST $;
@author     Jason Millward <jason@jcode.me>
@license    http://opensource.org/licenses/MIT
"""


def ping(version):
    """
        Send a simple ping to my server
            to see how many people are using this script
    """
    try:
        import uuid
        import requests
        import json
        import os
        import time

        data = {
            "uuid": uuid.getnode(),
            "version": version
        }

        dateFile = "/tmp/%s" % time.strftime("%Y%m%d")

        if not os.path.isfile(dateFile):

            with open(dateFile, 'w'):
                os.utime(dateFile, None)

            requests.post(
                'http://api.jcode.me/autorippr/stats',
                data=json.dumps(data),
                timeout=5
            )

    except:
        pass