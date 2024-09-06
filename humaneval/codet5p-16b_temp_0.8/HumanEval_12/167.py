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
    max_string = max(strings, key=len)
    return max(strings, key=len) if len(max_string) == len(strings[0]) else strings[0]
    # if len(strings) == 0:
    #     return None
    # else:
    #     return max(strings, key=len)

