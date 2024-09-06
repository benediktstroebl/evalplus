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

    # Handle empty list case
    if len(strings) == 0:
        return None

    # Initialize longest string
    longest = strings[0]

    # Loop over the strings
    for string in strings[1:]:
        if len(string) > len(longest):
            longest = string

    # Return longest string
    return longest

