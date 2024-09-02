from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    result = ''
    for c in strings:
        result += c
    return result

"""
You're given a series of JSON objects representing data about developers who have signed up to attend an event.
Write a function that returns a sorted array of the usernames (strings) of the developers who have signed up.
The return value should be sorted in alphabetical order.

Each JSON object will contain the following fields:
* first_name (string)
* last_name (string)
* email (string)
* company (string)
* created_at (string) This is the UTC timestamp of when the developer was created
* id (integer)

Your function should return the usernames (strings) in alphabetical order.

Assume that the developers were all created at the same time.
In other words, the following two inputs are equivalent:

concatenate(['{"first_name":"Aarushi", "last_name":"Tikka", "email":"A@gmail.com", "company":"lucas", "created_at":"2013-02-12T07:52:11Z", "id":1},
             {"first_name":"Akash", "last_name":"Sattar", "email":"A@gmail.com", "company":"lucas", "created_at":"2013-03-15T16:49:49Z", "id":2},
             {"first_name":"Anand", "last_name":"Khandelwal", "email":"Anand@gmail.com", "company":"lucas", "created_at":"2013-06-22T12:21:55Z", "id":3},
             {"first_name":"Anjana", "last_name":"Chowdhary", "email":"Anjana@gmail.com", "company":"lucas", "created_at":"2013-06-23T07:47:04Z", "id":4}])

concatenate(['{"first_name":"Aarushi", "last_name":"Tikka", "email":"A@gmail.com", "company":"lucas", "created_at":"2013-02-12T07:52:11Z", "id":1},
             {"first_name":"Akash",