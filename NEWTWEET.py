import requests
from requests_oauthlib import OAuth1
from dotenv import load_dotenv
import os


#OK the API keys are public so load_dotenv()
load_dotenv()


consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")



def random_quote():
    quote = requests.get("https://api.kanye.rest").json()
    return quote["quote"]


def format_fact_as_text(quote):
    return {"text": "{}".format(quote)}


def connect_to_oauth(consumer_key, consumer_secret, acccess_token, access_token_secret):
    url = "https://api.twitter.com/2/tweets"
    auth = OAuth1(consumer_key, consumer_secret, acccess_token, access_token_secret)
    return url, auth


def post():
    fact = random_quote()
    print("🐱 Fact:", fact)

    payload = format_fact_as_text(fact)
    print("📦 Payload:", payload)

    url, auth = connect_to_oauth(consumer_key, consumer_secret, access_token, access_token_secret)

    response = requests.post(
        auth=auth, url=url, json=payload, headers={"Content-Type": "application/json"}
    )

    print("📡 Status:", response.status_code)
    print("📬 Response:", response.text)

# Run test
post()


