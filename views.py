from django.shortcuts import render
from twilio.rest import Client
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

account_sid = "ACCOUNT_ID"
auth_token = "ACCOUT_TOKEN"
client = Client(account_sid, auth_token)

@csrf_exempt
def bot(request):
    sender = "SENDERNUMBER"
    if request.method == "POST":
        message_body = request.POST.get("Body", "").strip().lower()
        from_number = request.POST.get("From")

        if message_body == "hi":
            client.messages.create(
                body="Hello! How can I assist you today?",
                from_="whatsapp:{sender}",
                to=from_number
            )

    return HttpResponse("OK")
