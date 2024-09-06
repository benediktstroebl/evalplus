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

    longest_string: Optional[str] = None
    max_len: int = -1
    for string in strings:
        if len(string) > max_len:
            longest_string = string
            max_len = len(string)
    return longest_string

