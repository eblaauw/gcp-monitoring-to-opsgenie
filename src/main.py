from flask import abort
import os

AUTHENTICATION_TOKEN = os.environ.get("authentication_token", "default_token")
OPSGENIE_WEBHOOK = ""


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
    """[summary]

    Args:
        request: Incoming request

    Returns:
        str|func: Returns an 200 OK or an abort
    """
    if request.method == "POST":
        if verify_token(request.args.get("authentication_token")):
            json_object = request.get_json()
            opsgenie_object = {
                "message": json_object["incident"]["summary"],
                "alias": "Alias",
                "description": "GCP alert converted message",
                "priority": "P1",
            }
            return send_opsgenie_alert(opsgenie_object)
        else:
            return abort(405)
    return abort(405)


def send_opsgenie_alert(opsgenie_object):
    print(opsgenie_object)
    return "OK"
