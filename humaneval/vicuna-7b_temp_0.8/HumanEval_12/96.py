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
    max_len = max([len(s) for s in strings])
    if max_len == 0:
        return None
    elif max_len == 1:
        return strings[0]
    else:
        return strings[max_len - 1]

