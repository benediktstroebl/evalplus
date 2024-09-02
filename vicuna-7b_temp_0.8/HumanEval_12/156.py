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
    longest_str = max_len
    for s in strings:
        if len(s) > longest_str:
            longest_str = len(s)

    return longest_str.strip() if longest_str else None