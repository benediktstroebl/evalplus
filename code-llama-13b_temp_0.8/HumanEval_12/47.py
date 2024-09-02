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
    # Our implementation of this function would be very similar to our longest_string function.
    # However, we need to make a small adjustment to the base case
    if strings == []:
        return None
    # Keep track of the longest string seen so far
    longest_string = strings[0]
    for current in strings:
        # If the current string is longer than the longest_string we've seen so far, replace it
        if len(current) > len(longest_string):
            longest_string = current
    return longest_string

