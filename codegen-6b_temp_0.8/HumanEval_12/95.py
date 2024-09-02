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
    if len(strings) == 0:
        return None
    max_len = len(strings[0])
    for strng in strings:
        if len(strng) > max_len:
            max_len = len(strng)
    for strng in strings:
        if len(strng) == max_len:
            return strng

