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
    max_len = max([len(s) for s in strings])
    max_index = 0
    max_str = strings[0]
    for i in range(1, len(strings)):
        if len(strings[i]) > max_len:
            max_len = len(strings[i])
            max_index = i
            max_str = strings[i]
    return max_str