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

    # Dummy return value
    longest_string: Optional[str] = None

    # Loop through list and find longest string
    for string in strings:
        if longest_string is None or len(string) > len(longest_string):
            longest_string = string

    # If list was empty
    if longest_string is None:
        return None

    # Return longest string
    return longest_string

