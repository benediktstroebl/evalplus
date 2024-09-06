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

    longest_string = None

    # This is O(n) time complexity as we need to traverse the whole list of strings.
    # We use a for loop to iterate over each string.
    for string in strings:
        if longest_string is None or len(string) > len(longest_string):
            longest_string = string

    return longest_string

