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
    # if the input list is empty, return None
    if strings == []:
        return None

    # otherwise, get the maximum length in the input list
    max_len = max(len(x) for x in strings)

    # get the list of strings of the maximum length
    max_strings = [x for x in strings if len(x) == max_len]

    # return the first string of the maximum length
    return max_strings[0]

