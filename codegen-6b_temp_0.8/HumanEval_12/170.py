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
    len_longest = len(strings[0])
    longest = strings[0]
    for s in strings:
        len_s = len(s)
        if len_s > len_longest:
            longest = s
            len_longest = len_s
    return longest

