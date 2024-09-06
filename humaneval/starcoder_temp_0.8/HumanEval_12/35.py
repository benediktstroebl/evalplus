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
    # It's a tautology: if the list is empty, return None
    # >>> max([], default=None) is None
    # True
    # >>> longest([]) is None
    # True
    # >>> max([], key=len, default=None) is None
    # True
    # >>> longest([]) is None
    # True
    # If the list contains only one string, return that string
    # >>> max(['a'], default=None)
    # 'a'
    # >>> longest(['a'])
    # 'a'
    # >>> max(['a'], key=len, default=None)
    # 'a'
    # >>> longest(['a'])
    # 'a'
    # If the list contains multiple strings of the same length, return the first one
    # >>> max(['a', 'b', 'c'], default=None)
    # 'a'
    # >>> longest(['a', 'b', 'c'])
    # 'a'
    # >>> max(['a', 'bb', 'ccc'], default=None)
    # 'a'
    # >>> longest(['a', 'bb', 'ccc'])
    # 'a'
    if not strings:
        return None
    # If the list contains multiple strings of the same length, return the first one
    max_len = len(max(strings, key=len))
    return max(
        [
            string
            for string in strings
            if len(string) == max_len
        ],
        key=len
    )

