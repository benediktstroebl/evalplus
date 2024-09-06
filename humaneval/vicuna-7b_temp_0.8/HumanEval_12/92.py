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
    # Check for empty list
    if not strings:
        return None

    # Sort the list
    strings.sort()

    # Initialize the length of the longest string
    max_length = len(strings[0])

    # Initialize the longest string
    longest_string = strings[0]

    # Iterate through the list, updating the length and the longest string
    for s in strings:
        if len(s) > max_length:
            max_length = len(s)
            longest_string = s

    return longest_string
