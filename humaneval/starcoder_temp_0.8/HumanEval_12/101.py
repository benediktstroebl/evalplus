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

    # First, we find the longest string in strings by finding the max of the string's length
    # over the list of strings.
    if len(strings) == 0:
        return None

    longest_string = max(strings, key=len)

    # Then we return the first element of strings that is of the same length as longest_string.
    for string in strings:
        if len(string) == len(longest_string):
            return string

    return None

