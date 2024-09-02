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
    # empty list
    if not strings:
        return None

    # single-item list
    elif len(strings) == 1:
        return strings[0]

    # all strings have different length
    elif len(strings) == len(set(len(strings) for strings in strings)):
        return max(strings, key=len)

    # otherwise
    else:
        return max(strings, key=len)

