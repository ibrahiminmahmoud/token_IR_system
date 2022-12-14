import tweepy
import configparser
from tweepy.auth import OAuthHandler
import pandas as pd
#read config 

config=configparser.ConfigParser()
config.read('confg.ini')

api_key=config['twitter']['api_key']
api_key_secret=config['twitter']['api_key_secret']

access_token=config['twitter']['access_token']
access_token_secret=config['twitter']['access_token_secret']

#athu

auth=tweepy.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)



api=tweepy.API(auth)
search = tweepy.Cursor(api.search_tweets,q="hello",tweet_mode="extended").items(5)
#
columns=['Tweet']
data=[]

for tweets in search:
  data.append([tweets.full_text])
  df=pd.DataFrame(data,columns=columns)

df.to_csv('token.csv')