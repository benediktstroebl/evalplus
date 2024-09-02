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
    # We could have used min() as a starting value for the loop and if we found a new longest string,
    # we would replace it. But we want to return a string, not a single element of a list
    # so we can't use min()
    return max(strings, key=len) if strings else None

