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
    # I need to be careful about input validation!
    # I can use a sentinel value for None,
    # or I can raise an exception.
    if not strings:
        return None

    longest = strings[0]
    for i in range(1, len(strings)):
        if len(strings[i]) > len(longest):
            longest = strings[i]
    return longest

