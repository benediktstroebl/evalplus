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
    min_len = max(len(s) for s in strings)
    max_len = max(len(s) for s in strings)
    max_string = max(strings, key=len)
    return max_string[:max_len] if max_len != len(max_string) else None

