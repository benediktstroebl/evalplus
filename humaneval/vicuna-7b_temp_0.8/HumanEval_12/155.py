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
    max_len = min(len(s) for s in strings)
    max_index = 0
    max_val = max_len

    for index, s in enumerate(strings):
        if len(s) == max_len:
            max_val = index
        elif len(s) > max_len:
            max_len = len(s)
            max_index = index
            max_val = max_len

    return max_val

