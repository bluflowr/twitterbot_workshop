#!/usr/bin/env python
from twython import Twython
import random
import sys
from secret import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
from seuss import quotes

# Running script without -p does not post Tweet. 
# python tweet.py -p will post to twitter.
post_tweet = False
if len(sys.argv) > 1 and sys.argv[1] == "-p":
    post_tweet = True

# Initializing the twython object.
twitter = Twython(APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

def make_tweet():
	"""
	Generate a random tweet from listed quotes. 
	You can change this to generate a tweet in a different way.
	"""
	random_quote = random.choice(quotes)
	random_quote += " #seuss" #Adding in hashtags
	return random_quote


def tweet_out(tweet):
	"""
	Tweets out your status via the twython library. 
	If the tweet is between 1 and 140 characters long what should this function do?
	Try to fix it to look at tweet length!
	"""
	if post_tweet:
		twitter.update_status(status=tweet)
	else:
		print (tweet)

tweet_out(make_tweet()) #runs the tweet_out function