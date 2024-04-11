#!/usr/bin/python3
""" A module that queries the REDDIT API and returns the total
number of subscribers in a given subreddit"""
import requests


def number_of_subscribers(subreddit):
    """function to return no. of users or zero on failure"""
    subs = 0
    headers = {'User-agent': 'kirimiBot/0.0.1'}
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'
    r = requests.get(url, headers=headers, allow_redirects=False)
    if r.status_code == 200:
        data = r.json().get('data')
        if data:
            subs = data.get('subscribers')
    return subs
