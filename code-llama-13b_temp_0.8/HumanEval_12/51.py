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
    # return the first string in the list
    # if you find an empty list
    if not strings:
        return None
    longest_str = strings[0]
    # for each string in the list
    for string in strings:
        # if the length of the string is greater than the length of the longest string
        if len(string) > len(longest_str):
            # set the longest string to the current string
            longest_str = string
    # return the longest string
    return longest_str


    'name': 'Longest',
    'author': 'Anonymous',
    'url': 'http://mathforum.org/dr.math/faq/faq.longest.name.html',
    'created': '3rd century AD',
