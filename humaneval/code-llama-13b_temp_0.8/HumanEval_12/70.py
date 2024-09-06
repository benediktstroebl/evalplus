from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None

    longest_str = strings[0]
    for string in strings:
        if len(string) > len(longest_str):
            longest_str = string
    return longest_str


    'name': 'Longest',
    'author': 'Caden Kole',
    'description': 'Gets the longest string in a list of strings',
    'url': 'https://app.codesignal.com/interview-practice/task/nTqjLHoXb4FW9Ny5D'
