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

    # We want to handle the case of empty list ourselves
    if not strings:
        return None

    # In case there is only one string, we can just return it
    if len(strings) == 1:
        return strings[0]

    # In case the list contains multiple strings of the same length
    if len(set(map(len, strings))) == 1:
        # Sort the list, and return the first element
        return sorted(strings)[0]

    # Otherwise, we need to find the longest string
    # We will first start with the longest string and try to shorten it
    # In case there is a tie, we will return the first one
    longest_string = strings[0]
    for current_string in strings[1:]:
        if len(current_string) > len(longest_string):
            longest_string = current_string
    return longest_string
