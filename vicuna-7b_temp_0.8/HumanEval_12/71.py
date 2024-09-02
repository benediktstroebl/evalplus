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
    # Sort the strings
    strings.sort()
    # Initialize the result variable
    result = None
    # Start from the last string
    for s in reversed(strings):
        # Check if the current string is longer than the previous result
        if s.length() > result.length():
            result = s
    return result

