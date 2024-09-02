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
    # If the input list is empty, return None
    if not strings:
        return None

    # Find the maximum length of the strings in the list
    max_len = 0
    for string in strings:
        if len(string) > max_len:
            max_len = len(string)

    # If there is only one string, return it
    if len(strings) == 1:
        return strings[0]

    # If there are multiple strings, return the first one that is longer than the maximum length
    for string in strings:
        if len(string) > max_len:
            return string

    # If all strings are shorter than the maximum length, return None
    return None

