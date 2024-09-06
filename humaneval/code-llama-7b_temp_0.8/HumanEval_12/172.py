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

    # Initially, the longest string is the first string in the input list
    longest_string = strings[0]

    # Iterate through the list to see if there is a longer string
    for string in strings[1:]:
        if len(string) > len(longest_string):
            longest_string = string

    return longest_string

