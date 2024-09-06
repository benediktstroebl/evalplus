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
    # 1. filter out empty strings
    strings = [string for string in strings if string != ""]

    # 2. check if list is empty
    if len(strings) == 0:
        return None

    # 3. get the longest string
    return sorted(strings, key=len)[-1]

