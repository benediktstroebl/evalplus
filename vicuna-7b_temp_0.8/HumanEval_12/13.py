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
    # sort the list of strings in lexicographic order
    strings.sort()
    # find the maximum length of the strings in the list
    max_len = len(strings[0])
    for string in strings[1:]:
        if len(string) > max_len:
            max_len = len(string)
    # return the first string if there is more than one with the same length, or None if the list is empty
    return strings[0] if max_len > len(strings[0]) else None

