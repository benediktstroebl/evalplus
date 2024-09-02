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

    # Sort the list based on the length of the string.
    # Sort the list based on the length of the string.
    # Use the last element of sorted list as the first element.
    # This ensures that the string with
    # the largest length will be at the first position.
    strings = sorted(strings, key=lambda x: len(x))
    strings[0], strings[-1] = strings[-1], strings[0]

    return strings[0]

