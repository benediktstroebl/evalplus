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

    max_len = len(strings[0])
    min_len = max_len
    for s in strings:
        if len(s) > max_len:
            max_len = len(s)
        if len(s) < min_len:
            min_len = len(s)
    return strings[0]

