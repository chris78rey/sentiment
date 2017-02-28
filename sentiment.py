import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'SdvhpZE6C0HdQZeMWJ5eLAEoW'
consumer_secret= 'yYCcU9ejpt0qyMkeXwBhdOb1joymdv2zFw7fWdtNXWd3Vyldqe'

access_token='712760194502098945-BjePQ9eEsTM0Lrioq3ihiAIsTS9MW2X'
access_token_secret='URC5CPBoLMxd2tJo9Mehs2rKevluFJoPaYw5aFMLRCFZX'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('donald trump')

for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
