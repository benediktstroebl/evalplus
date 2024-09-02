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
    max_index = 0
    for i in range(1, len(strings)):
        if len(strings[i]) > len(strings[max_index]):
            max_index = i
    return strings[max_index]

