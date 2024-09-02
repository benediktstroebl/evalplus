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
    longest_so_far: Optional[str] = None
    for string in strings:
        if not string:
            continue
        if longest_so_far is None or len(string) > len(longest_so_far):
            longest_so_far = string
    return longest_so_far

