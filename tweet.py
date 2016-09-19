from twython import Twython
import random
from secret import APP_KEY, APP_SECRET, OAUTH_TOKEN, OAUTH_TOKEN_SECRET
from seuss import quotes

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


def new_tweet(tweet):
	"""
	Tweets out your status via the twython library if the
	tweet is between 1 and 140 characters long. If it is not,
	it'll request another generated tweet from the make_tweet function. 
	"""
	if len(tweet) > 1 and len(tweet) < 140:
		twitter.update_status(status=tweet)
	else:
		new_tweet(make_tweet())

new_tweet(make_tweet()) #runs the new_tweet function