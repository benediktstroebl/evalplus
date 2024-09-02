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
    # a = 1, b = 11, c = 111
    # a < b, b < c
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    # 1, 11, 21, 121, 111, 1211, 1221, 1231, 1232, 1233, ...
    # If a = 1, b = 11, c = 111, c is the max.
    # If a = 11, b = 111, c = 121, a is the max
    # If a = 111, b = 1211, c = 1231, b is the max
    #
    # For strings,
    # a < b, b < c
    # 1 < 11 < 111 < ...
    # If a = 'a', b = 'bb', c = 'ccc', c is the max.
    # If a = 'bb', b = 'bbb', c = 'bbbb', a is the max
    # If a = 'bbbb', b = 'bbbbb', c = 'bbbbbb', b is the max
    #
    # For a specific case, a is the max.
    # For a specific case, b is the max.
    # For a specific case, c is the max.
    # For multiple specific cases, a is the max.

    strings.sort()
    return strings[-1] if strings else None

