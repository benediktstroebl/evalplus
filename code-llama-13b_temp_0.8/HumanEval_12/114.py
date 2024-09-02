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
    # Don't do anything if there is no string to check
    if not strings:
        return None

    # Initialize the longest string and its length
    longest_string = strings[0]
    longest_len = len(longest_string)

    # Iterate over the strings to find the longest one
    for string in strings:
        if len(string) > longest_len:
            longest_string = string
            longest_len = len(longest_string)

    return longest_string

