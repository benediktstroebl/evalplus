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

    if len(strings) == 1:
        return strings[0]

    max_string_length = len(strings[0])
    longest_string = strings[0]

    for string in strings[1:]:
        if len(string) > max_string_length:
            max_string_length = len(string)
            longest_string = string

    return longest_string

