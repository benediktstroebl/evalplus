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
    # TODO: 1. Implement this function.


    # sort the list of strings by their length
    sorted_strings = sorted(strings, key=len)

    # if the input list is empty, return None
    if not sorted_strings:
        return None

    # return the first string in the sorted list
    return sorted_strings[0]

