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

    longest_str: str = strings[0]

    for curr_str in strings:
        if len(curr_str) > len(longest_str):
            longest_str = curr_str

    return longest_str

