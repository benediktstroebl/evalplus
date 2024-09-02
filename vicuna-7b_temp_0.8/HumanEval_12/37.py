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
    max_len = min_len = 0
    max_len_index = max_len_index = None
    for s in strings:
        len_s = len(s)
        if len_s > max_len:
            max_len = len_s
            max_len_index = len(strings) - len_s
        if len_s < min_len:
            min_len = len_s
    if max_len_index is not None:
        return strings[max_len_index]
    return None

