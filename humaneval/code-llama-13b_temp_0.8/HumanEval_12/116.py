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
    # Initialize longest string and its length
    longest_str = strings[0]
    len_longest_str = len(longest_str)
    # Loop through string and compare the current one to the longest one
    for i in range(len(strings)):
        if len_longest_str < len(strings[i]):
            longest_str = strings[i]
            len_longest_str = len(longest_str)
    return longest_str

