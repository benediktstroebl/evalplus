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

    longest_string = ''
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string
    # if len(strings) > 0:
    #     return max(strings, key=len)
    # else:
    #     return None
    # return None
    # return max(strings, key=len)

