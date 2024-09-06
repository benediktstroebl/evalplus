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
    # if the input is of length 1, return the string
    # if the input is of length 0, return None
    # if the input contains duplicate strings, return the first string
    if len(strings) < 1:
        return None
    if len(strings) == 1:
        return strings[0]
    # take first string as the max
    max_string = strings[0]
    for string in strings:
        if len(string) > len(max_string):
            max_string = string
    return max_string

