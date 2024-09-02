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
    max_index = 0
    max_length = 0
    for index, string in enumerate(strings):
        if len(string) > max_length:
            max_index = index
            max_length = len(string)
    return strings[max_index]

