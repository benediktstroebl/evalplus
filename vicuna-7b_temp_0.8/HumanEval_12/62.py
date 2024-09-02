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
    if max_len == len(strings[0]):
        return strings[0]
    max_index = 0
    max_str = strings[0][:max_len]
    for i, s in enumerate(strings):
        if len(s) > max_len:
            max_len = len(s)
            max_str = s[max_len:] + max_str
            max_index = i
    return max_str

