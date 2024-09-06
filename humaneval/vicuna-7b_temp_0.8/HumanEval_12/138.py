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
    max_length = max(len(s) for s in strings)
    max_index = None
    for i, s in enumerate(strings):
        if len(s) > max_length:
            max_length = len(s)
            max_index = i
    return max_length, max_index

