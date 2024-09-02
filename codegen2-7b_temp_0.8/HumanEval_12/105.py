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
    if strings == []:
        return None
    strings_set = set(strings)
    if len(strings_set) == 1:
        return strings_set.pop()
    else:
        return max(strings_set, key=len)
