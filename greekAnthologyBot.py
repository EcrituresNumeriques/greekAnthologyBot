# This bot tweets random epigrams retrived by the api of the Greek Anthology project of the CRC in digital textualities
import json
import urllib
url = 'http://anthologia.ecrituresnumeriques.ca/api/v1/entities'
##parsing response
response = urllib.urlopen(url)
cont = json.loads(response.read().decode('utf-8'))

countVersion = 0


 # counting avaiable versions
for item in cont:
	countVersion += 1
	counter = 0
	for text in item['versions']: 
		counter += 1  
		


from random import randint
randomVersion = (randint(0, countVersion))  
countTexts = 0	
for textrandom in cont[randomVersion]['versions']:
	countTexts += 1	
	
	randomText = (randint(0, countTexts))

	
	tweetLong = (textrandom['text_translated'])

	
tweet = (tweetLong[0:139])


import tweepy

consumer_key = 'yourKey'
consumer_secret = 'yourKey'
access_token = 'yourKey'
access_token_secret = 'yourKey'
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)


api.update_status(tweet)  
