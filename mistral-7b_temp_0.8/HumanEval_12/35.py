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
        max_len = len(strings[0])
        max_str = ""
        for i in range(len(strings)):
            if len(strings[i]) >= max_len:
                max_len = len(strings[i])
                max_str = strings[i]
        return max_str

