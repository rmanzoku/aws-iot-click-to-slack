import os
import json
import logging
import urllib.request
import urllib.parse


logger = logging.getLogger()
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    webhook_url = os.environ.get('WEBHOOK_URL')

    logger.info('Received event: ' + json.dumps(event))

    text = '''
    %s %s
    ''' % (
        event["placementInfo"]["placementName"],
        event["placementInfo"]["attributes"].get("msg")
    )

    body = {
        "link_names": 1,
        'username': event["placementInfo"]["attributes"].get("username", "AWS IoT"),
        'text': text,
        'icon_emoji': event["placementInfo"]["attributes"].get("icon_emoji", ":aws:")
    }

    encoded_post_data = urllib.parse.urlencode({"payload": body}).encode(encoding='ascii')
    urllib.request.urlopen(url=webhook_url, data=encoded_post_data)
