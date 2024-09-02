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
    longest_length = -1
    longest_string = None

    for string in strings:
        length = len(string)
        if length > longest_length:
            longest_length = length
            longest_string = string

    return longest_string

