#!/usr/bin/python3
# script to gather data from an API
# get users names from the API
import requests
import sys


def get_username(base_url, user_id):
    """Gets usernames
       Args:
           base_url (str): base url for API
           user_id (str): user id numbers
       Returns: username
    """
    response = requests.get(
        "{}users/{}".format(base_url, user_id))
    usr_dict = response.json()
    return usr_dict['name']


def get_todo_list(base_url, user_id):
    """Gets todo list
       Args:
           base_url (str): base url for API
           user_id (str): user id numbers
       Returns: list of todo items (dicts)
    """
    response = requests.get(
        "{}users/{}/todos".format(base_url, user_id))
    return response.json()


def get_completed(todo_list):
    """Gets completed items
       Args:
           todo_list (list): list of todo items
<<<<<<< HEAD
       Returns: string of todo items to prints
=======
       Returns: string of todo items to prints~
>>>>>>> 85771a53aab761c2c8cf3bf78c8b570c17a56c12
    """

    done_str = ""
    done_list = []
    count = 0
    for todo in todo_list:
        if todo['completed'] is True:
            count += 1
            done_list.append("\t {}".format(todo['title']))
    done_str = "\n".join(done_list)

    return count, done_str


if __name__ == '__main__':
    user_id = sys.argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/'

    uname = get_username(base_url, user_id)
    todo_list = get_todo_list(base_url, user_id)
    total = len(todo_list)

    count, done_str = get_completed(todo_list)

    print(
        "Employee {} is done with tasks({}/{}):".format(uname, count, total))
    if count > 0:
        print(done_str)
