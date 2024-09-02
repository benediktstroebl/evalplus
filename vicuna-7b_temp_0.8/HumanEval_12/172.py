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
    max_len = max(len(s) for s in strings)
    for s in strings:
        if len(s) > max_length and len(s) == max_len:
            max_length = len(s)
            max_len = max_len
    return max_len