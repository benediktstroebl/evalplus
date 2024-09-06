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
    if len(strings) == 0:
        return None

    # First, we want to sort the strings, to compare the length of each
    # string with the current longest string
    strings = sorted(strings, key=lambda x: len(x), reverse=True)

    # Then, we want to iterate over the sorted strings and select the
    # longest one
    longest_string = strings[0]
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string

    return longest_string

