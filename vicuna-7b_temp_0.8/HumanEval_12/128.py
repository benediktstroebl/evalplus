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
    # Set the length of the first string
    max_length = max(len(s) for s in strings)

    # If all strings are empty, return None
    if not strings:
        return None

    # If there's only one string, return it
    if len(strings) == 1:
        return strings[0]

    # Otherwise, sort the strings and take the first one
    sorted_strings = sorted(strings, key=lambda s: s.lower())
    return sorted_strings[0]

