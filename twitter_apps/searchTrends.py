import twitter

twitter_api = twitter.Twitter(domain='api.twitter.com', api_version='1')
trends = twiiter_api.trends()

[ trend['name'] for trend in trends['trends'] ]
