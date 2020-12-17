import tweepy
from config import create_api

class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()
    def on_status(self, tweet):
        print(tweet.text)
    def on_error(self, status):
        print(status)



def main():
    api = create_api()
    listener = MyStreamListener(api)
    stream = tweepy.Stream(api.auth, listener)
    stream.filter(track=["Python", "Django"], languages="en")


main()