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

    if len(strings) == 1:
        return strings[0]

    length = len(strings[0])
    max_str = strings[0]

    for s in strings:
        if len(s) > length:
            length = len(s)
            max_str = s

    return max_str

