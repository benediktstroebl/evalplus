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
    max_idx = 0
    max_len = max_length
    for idx, s in enumerate(strings):
        if len(s) > max_len:
            max_len = len(s)
            max_idx = idx
    return strings[max_idx]

