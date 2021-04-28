from flask import abort
import os
import requests
import json

AUTHENTICATION_TOKEN = os.environ.get("AUTHENTICATION_TOKEN", "default_token")
OPSGENIE_WEBHOOK_URL = os.environ.get(
    "OPSGENIE_WEBHOOK_URL", "https://api.opsgenie.com/v2/alerts"
)
OPSGENIE_API_TOKEN = os.environ.get(
    "OPSGENIE_API_TOKEN", ""
)


def verify_token(given_token):
    """Verify the token which is being passed as an parameter

    Args:
        given_token (str): Given token

    Returns:
        bool: Returns the result of the token verification
    """
    if given_token == AUTHENTICATION_TOKEN:
        return True
    return False


def handler(request):
    """Collect the request, validate the request and send the request to send_opsgenie_alert

    Args:
        request: Incoming request
    """
    if request.method == "POST":
        if verify_token(request.args.get("authentication_token")):
            json_object = request.get_json()
            return send_opsgenie_alert(json_object)
        else:
            return abort(405)
    return abort(405)


def send_opsgenie_alert(json_object):
    """Sends an alert to opsgenie

        Args:
            json_object: Sends the formatted JSON to the Opsgenie server
        """
    message = str(
        "[GCP Message]: "
        + json_object["incident"]["condition_name"]
        + " "
        + json_object["incident"]["resource_name"]
    )
    headers = {
        "Authorization": "GenieKey " + OPSGENIE_API_TOKEN,
        "Content-Type": "application/json",
    }
    opsgenie_object = {
        "message": message,
        "alias": "Alias",
        "description": json_object["incident"]["summary"],
        "priority": "P1",
    }
    try:
        re = requests.post(
            OPSGENIE_WEBHOOK_URL, data=json.dumps(opsgenie_object), headers=headers
        )
        re.raise_for_status()
        return "OK"
    except Exception as exception:
        print(exception)
        raise
