# Crypto Price Alert System (Cryptoo)

This is a Python script that monitors the price of a specified cryptocurrency using the CoinGecko API and sends an SMS alert using Twilio if the price crosses a defined threshold.

## Features
- Fetches the current price of a cryptocurrency using the CoinGecko API.
- Sends an SMS alert to your phone using Twilio if the price falls below a specified threshold.
- Easy to customize and use for different cryptocurrencies and price thresholds.

## Requirements
- Python 3.x
- `requests` library: `pip install requests`
- `twilio` library: `pip install twilio`

## Setup Instructions
1. Clone this repository to your local machine.
2. Install the required Python packages using `pip install -r requirements.txt`.
3. Replace the placeholders in the script with your Twilio account details:
   - `account_sid`: Your Twilio Account SID.
   - `auth_token`: Your Twilio Auth Token.
   - `from_phone_number`: Your Twilio phone number.
   - `to_phone_number`: The phone number where you want to receive the alert.
4. Customize the `crypto_id`, `threshold_price`, and `check_interval` parameters in the script to suit your needs.
5. Run the script to start monitoring the cryptocurrency price.

## Example Usage
```python
crypto_id = "bitcoin"  # Cryptocurrency to monitor 
threshold_price = 60030  # Alert if price falls below this threshold
to_phone_number = "+1234567890"  # Your phone number

monitor_crypto_price(crypto_id, threshold_price, to_phone_number)
