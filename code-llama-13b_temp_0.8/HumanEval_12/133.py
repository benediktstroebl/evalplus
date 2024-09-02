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
    max_length = 0
    result = None

    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            result = string
    return result


    'name': 'Longest string',
    'author': 'Anonymous',
    'description': 'Returns the longest string. Returns the first one in case of multiple strings '
                   'of the same length',
    'url': 'https://mathlesstraveled.com/etymology/longest-string',
    'source': 'first_attempt.py'
