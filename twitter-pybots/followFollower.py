import tweepy
import time
from config import create_api

def follow_follower(api):
    for follower in tweepy.Cursor(api.followers).items():
        if not follower.following:
            try:
                follower.follow()
            except TweepError as e:
                print("Already requested")

def main():
    api = create_api()
    while True:
        follow_follower(api)
        time.sleep(60)

if __name__ == "__main__":
    main()