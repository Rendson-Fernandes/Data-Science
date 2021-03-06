import datetime
from email.utils import mktime_tz, parsedate_tz
from TwitterSearch import *


def format_date(value):
    time_tuple = parsedate_tz(value)
    timestamp = mktime_tz(time_tuple)
    return str(datetime.datetime.fromtimestamp(timestamp))


TwitterConnect = TwitterSearch(
    consumer_key='',
    consumer_secret='',
    access_token='',
    access_token_secret='',
 )


Search = TwitterSearchOrder()
Search.set_keywords(['bolsonaro'])
Search.set_language('pt')
# Search.set_negative_attitude_filter()
# Search.set_positive_attitude_filter()

for tweet in TwitterConnect.search_tweets_iterable(Search):
    if tweet['truncated'] == 0:
        print((format_date(tweet['created_at']) + ' @' + tweet['user']['screen_name'] + ' tweeted: ' + tweet['text']))
        # print(tweet)

