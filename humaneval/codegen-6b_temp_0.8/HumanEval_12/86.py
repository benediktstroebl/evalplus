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
    max_len = len(strings[0])
    for string in strings:
        if len(string) > max_len:
            max_len = len(string)
    max_string = strings[0]
    for string in strings[1:]:
        if len(string) == max_len:
            max_string = max_string if max_string > string else string
    return max_string

