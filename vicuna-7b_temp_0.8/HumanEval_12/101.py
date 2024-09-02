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
    # Sort the list of strings in descending order of length
    strings = sorted(strings, key=len, reverse=True)
    # Return the first string if there is only one string
    if len(strings) == 1:
        return strings[0]
    # Return the longest string
    return strings[-1]

