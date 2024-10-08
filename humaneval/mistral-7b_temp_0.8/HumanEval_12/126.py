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
    max_length = len(strings[0])
    max_index = 0
    for i in range(1, len(strings)):
        if max_length < len(strings[i]):
            max_length = len(strings[i])
            max_index = i
    return strings[max_index]
