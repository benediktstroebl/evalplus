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
    # your code here
    longest_so_far = ''
    for string in strings:
        if len(string) > len(longest_so_far):
            longest_so_far = string
    return longest_so_far

