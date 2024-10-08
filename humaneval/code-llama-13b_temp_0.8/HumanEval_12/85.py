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
    longest_str = max(strings, key=len)
    longest_str_length = len(longest_str)
    longest_strs = list(filter(lambda s: len(s) == longest_str_length, strings))
    return min(longest_strs, key=strings.index)

