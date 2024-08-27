import requests
from twilio.rest import Client
import time

# ---------------------------------------Function to fetch current price of a cryptocurrency using CoinGecko API------------------------------
def get_crypto_price(crypto_id, currency='usd'):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={crypto_id}&vs_currencies={currency}"
    response = requests.get(url)
    print(f"API Response Status Code: {response.status_code}")  # This will print the status code to check if the request is successful
    data = response.json()
    return data[crypto_id][currency]

# ---------------------------------------Function to send an SMS alert using Twilio------------------------------
def send_sms_alert(body, to_phone_number):
    account_sid = 'Replace with your Twilio Account SID'  
    auth_token = 'Replace with your Twilio Auth Token'
    from_phone_number = 'Replace with your Twilio phone number

    # ------------Create a Twilio client---------------
    client = Client(account_sid, auth_token)

    # Send the SMS message
    message = client.messages.create(
        body=body,
        from_=from_phone_number,
        to=to_phone_number
    )
    #print(f"SMS Message SID: {message.sid}")

# ------------Function to monitor the price and send an alert if it crosses the threshold----------------
def monitor_crypto_price(crypto_id, threshold_price, to_phone_number, check_interval=30):
    try:
        while True:
            current_price = get_crypto_price(crypto_id)
            print(f"Current price of {crypto_id}: ${current_price}")

            if current_price < threshold_price:
                send_sms_alert(
                    body=f"The price of {crypto_id.capitalize()} has crossed your threshold. Current price: ${current_price}",
                    to_phone_number=to_phone_number
                )
                print("Alert sent! Price is below the threshold go and buy now hurry up Avinash.")
                break  # Stop monitoring after the alert is sent

            time.sleep(check_interval)  # Wait before checking the price again
    except Exception as e:
        print(f"An error occurred: {e}")

# ---------Example Usage
crypto_id = "bitcoin"  # Cryptocurrency to monitor 
threshold_price = 60030
to_phone_number = "enter mobile no where you want to receive a notification sms"

# ------------Uncomment the following line to run the monitor
monitor_crypto_price(crypto_id, threshold_price, to_phone_number)
