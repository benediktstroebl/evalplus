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
    # If there is no element, the longest string is None
    if len(strings) == 0:
        return None

    # the longest string is the one with maximum length
    max_string = strings[0]
    max_length = len(max_string)
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            max_string = string

    return max_string

