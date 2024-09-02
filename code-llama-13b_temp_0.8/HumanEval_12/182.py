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
    result = None
    if len(strings) != 0:
        longest_length = 0
        for s in strings:
            if len(s) > longest_length:
                longest_length = len(s)
                result = s
    return result


