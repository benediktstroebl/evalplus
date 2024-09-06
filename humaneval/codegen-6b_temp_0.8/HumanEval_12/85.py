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

    # Sort the list according to the length of the strings in reverse order
    # (the greater the length, the earlier the string)
    longest_string_ids = sorted(range(len(strings)), key=lambda k: len(strings[k]), reverse=True)

    # return the first element of the list
    return strings[longest_string_ids[0]]

