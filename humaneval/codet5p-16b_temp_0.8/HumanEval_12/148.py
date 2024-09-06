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

    longest_one = None
    longest_len = 0

    if strings:
        longest_one = strings[0]
        longest_len = len(strings[0])
        for string in strings[1:]:
            if len(string) > longest_len:
                longest_len = len(string)
                longest_one = string

    return longest_one

