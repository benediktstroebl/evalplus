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
    longest_len = 0
    longest_str = ''
    for str in strings:
        if len(str) > longest_len:
            longest_len = len(str)
            longest_str = str
    if len(longest_str) == 0:
        return None
    return longest_str

