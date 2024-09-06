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
    # if empty list
    if not strings:
        return None

    # if only one string, return it
    elif len(strings) == 1:
        return strings[0]

    # initialize variables
    longest = strings[0]
    current = strings[0]

    # iterate through the list
    for i in range(1, len(strings)):
        # if len[current] is greater than len[longest]
        if len(current) > len(longest):
            # update longest
            longest = current
        # if len[current] is equal to len[longest]
        elif len(current) == len(longest):
            # if current is in the middle of a substring of longests
            if current in longest:
                # update longest
                longest = current
        # if current is longer than longest
        elif len(current) > len(longest):
            # update longest
            longest = current

        # update current
        current = strings[i]

    return longest

"""
Terminal

"""

