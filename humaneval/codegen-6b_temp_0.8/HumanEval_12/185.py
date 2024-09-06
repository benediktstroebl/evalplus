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
    str_len = len(strings)
    max_str = strings[0]
    for i in range(1, str_len):
        if len(strings[i]) > max_len:
            max_str = strings[i]
            max_len = len(max_str)
    return max_str

