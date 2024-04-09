#!/usr/bin/python3
"""
The number of subscribers function
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for the given subreddit"""
    if subreddit is None or type(subreddit) is not str:
        return 0
    r = requests.get(
        "http://www.reddit.com/r/{}/about.json".format(subreddit)
    ).json()
    subs = r.get("data", {}).get("subscribers", 0)
    return subs