import requests

API_KEY = "fca_live_rppWa9uViJWZsLepWorz9qoIPaSGqwsE7CRkQDnv"
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "AUD", "INR"]

def convert_currency(base):
	currencies = ",".join(CURRENCIES)
	url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
	print(url)
	try:
		response = requests.get(url)
		data = response.json()
		return data
	except Exception as e:
		print(f"The following exception occurred : {e}")
		return None


if __name__ == "__main__":
	data = convert_currency("INR")
	print(data['data'])