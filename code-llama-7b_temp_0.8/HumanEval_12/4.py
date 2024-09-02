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
    # If there are no strings, return None
    if not strings:
        return None

    # If there is one string, return it.
    if len(strings) == 1:
        return strings[0]

    # Go through the strings and find the longest one
    longest_string = strings[0]
    for string in strings[1:]:
        if len(string) > len(longest_string):
            longest_string = string

    return longest_string

