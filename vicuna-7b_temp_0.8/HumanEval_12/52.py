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
    max_len = min_len = 0
    max_string = ""
    min_string = ""
    for string in strings:
        len_string = len(string)
        if len_string > max_len:
            max_len = len_string
            max_string = string
        elif len_string < min_len:
            min_len = len_string
            min_string = string
    return max_string

