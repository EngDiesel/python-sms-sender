from twilio.rest import Client

account_sid = 'ACe4d6a181f625f78d4e187e7d7929c912'
auth_token = 'a252af04329f84eec4cb8464b296be04'

client = Client(account_sid, auth_token)

# FROM = '+1 202 804 2271'
FROM = '+1 202 804 2279'



def send_message(message, to, _from_=FROM):
    """
    This is a simple message sender function
    based on `twilio` API

    params: `message` ->  The body of the message that you
                        wish to send.

            `to` ->       The Phone Number you are attempting to send
                        the message to.
    """

    try:
        msg = client.messages.create(
                                      from_=_from_,
                                      body=message,
                                      to=to
                                  )
        print("Successfully sent the message: %s \n To: %s" % (message, to))

    except Exception as e:
        print("An error has occured wile sending the message to %s \n the \
        error message: %s" % (to, str(e)))

    return
