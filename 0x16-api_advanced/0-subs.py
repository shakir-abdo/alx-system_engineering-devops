#!/usr/bin/python3
"""
Returns the number of subs of a reddit sub
"""

import requests


def number_of_subscribers(subreddit):
    """returns the number of subscribers for a given subreddit"""
    headers = {"User-Agent": "Mozilla/5.0, ALX project"}

    if not subreddit:
        return 0
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json()["data"]["subscribers"]
