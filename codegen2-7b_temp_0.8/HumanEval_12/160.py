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
    else:
        max_length = 0
        max_string = strings[0]
        for i in range(0, len(strings)):
            if len(strings[i]) > max_length:
                max_length = len(strings[i])
                max_string = strings[i]
        return max_string
