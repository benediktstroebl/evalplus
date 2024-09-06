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
    max_len = max(len(s) for s in strings)
    max_idx = 0
    for idx, s in enumerate(strings):
        if len(s) == max_len:
            return s
        if idx + 1 < len(strings) and len(s) < len(strings[idx + 1]):
            max_len = len(strings[idx + 1])
            max_idx = idx + 1
    return None

