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
    # if the list is empty, return None
    if not strings:
        return None

    # if the list contains only one element, return it
    if len(strings) == 1:
        return strings[0]

    # sort the list by length
    strings.sort(key=len, reverse=True)

    # check if the list has only one element
    if len(strings) == 1:
        return strings[0]

    # calculate the maximum length in the list
    max_length = max(len(s) for s in strings)

    # if the list is empty, return None
    if max_length == 0:
        return None

    # return the first string that is longer than the maximum length
    for s in strings:
        if len(s) > max_length:
            return s

    # if no string is longer than the maximum length, return None
    return None

