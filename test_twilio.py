import keys2
from twilio.rest import Client

client = Client(keys2.accountSID, keys2.authToken)

TwilioNumber= '+12058963685'
myCellphone = '+12513480758'

textmsg = client.messages.create(to=myCellphone, from_=TwilioNumber, body='You are stinky!')

print(textmsg.status)

call = client.calls.create(url='http://demo.twilio.com/docs/voice.xml', to=myCellphone, from_=TwilioNumber)