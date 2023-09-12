from django.shortcuts import render, redirect  
import requests
import json
# Create your views here.


#  <=================================================================================================     Functions here    ============================================================================================================================================>
# Function to return to call the thml file in the templates folder
def home(request):
    # functions here for now it only redirects to a link 
   return render(request, 'frontend/index.html')

import requests
from django.shortcuts import render  # Import the appropriate render function

def paymongo(request):
    url = "https://api.paymongo.com/v1/checkout_sessions"
    payload = {
        "data": {
            "attributes": {
                "send_email_receipt": False,
                "show_description": True,
                "show_line_items": True,
                "line_items": [
                    {
                        "currency": "PHP",
                        "amount": 30000,
                        "name": "name",
                        "quantity": 1,
                        "description": "text"
                    }
                ],
                "payment_method_types": ["gcash","card"],
                "description": "text"
            }
        }
    }
    headers = {
        "accept": "application/json",
        "Content-Type": "application/json",
        "authorization": "Basic c2tfdGVzdF9QV2FyVWtSTDFjcXhhZTdtV1h4SEZ2NGg6"
    }
    response = requests.post(url, json=payload, headers=headers)
    response_data = response.json()  # Parse response content as JSON
    checkout_url = response_data["data"]["attributes"]["checkout_url"]
    return redirect(checkout_url)
