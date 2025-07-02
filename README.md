---

# 📱 WhatsApp Bot using Django + Twilio

This project demonstrates a simple WhatsApp bot built with Django and Twilio API. When a user sends `"hi"`, the bot responds with a greeting.

---

## ✅ Features

* Receive WhatsApp messages via Twilio webhook
* Respond to specific messages (like `"hi"`) with automated replies
* Deployed using `ngrok` for local testing

---

## 🛠️ Requirements

* Python 3.x
* Django
* Twilio Account + Sandbox
* Ngrok (for exposing local server to the internet)

---

## 🚀 Setup & Execution

Follow the steps below to get the bot up and running.

### 1. Clone or Create a New Django Project

```bash
django-admin startproject whatsappBot
cd whatsappBot
python3 manage.py startapp bot
```

### 2. Add App to Installed Apps

Open `whatsappBot/settings.py` and add `'bot'` to the `INSTALLED_APPS` list:

```python
INSTALLED_APPS = [
    ...
    'bot',
]
```

---

### 3. Configure URL

Edit `whatsappBot/urls.py`:

```python
from django.contrib import admin
from django.urls import path
from bot.views import bot

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bot/', bot),  # Webhook endpoint for Twilio
]
```

---

### 4. Install Dependencies

```bash
pip install django twilio
```

---

### 5. Add the Bot Logic

Inside `bot/views.py`, paste:

```python
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from twilio.rest import Client

account_sid = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Replace with your SID
auth_token = "your_auth_token"                    # Replace with your token
client = Client(account_sid, auth_token)

@csrf_exempt
def bot(request):
    if request.method == "POST":
        message_body = request.POST.get("Body", "").strip().lower()
        from_number = request.POST.get("From")

        if message_body == "hi":
            client.messages.create(
                body="Hello! How can I assist you today?",
                from_="whatsapp:+14155238886",
                to=from_number
            )

    return HttpResponse("OK")
```

---

### 6. Apply Migrations & Run Server

```bash
python3 manage.py migrate
python3 manage.py runserver 8080
```

---

### 7. Expose Localhost using Ngrok

In a new terminal:

```bash
ngrok http 8080
```

Copy the `https://xxxxxx.ngrok.io` URL.

---

### 8. Configure Twilio Sandbox Webhook

1. Go to [Twilio Console > Messaging > Try it Out > Send a WhatsApp message](https://www.twilio.com/console/sms/whatsapp/learn)
2. Paste your webhook URL:

   ```
   https://xxxxxx.ngrok.io/bot/
   ```
3. Save and send a message like `"hi"` to the Twilio sandbox number.

---

## 🧪 Example

Send:

```
hi
```

You’ll receive:

```
Hello! How can I assist you today?
```

---

## 📝 Notes

* Make sure your Twilio Sandbox is set up correctly and your WhatsApp number is joined to it.
* The webhook URL must be public (use `ngrok` or deploy to a server).
* You can extend the bot logic to handle more keywords and workflows.

---

