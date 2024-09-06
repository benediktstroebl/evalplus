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
    return max(strings, key=len)
    # return None if strings == [] else max(strings, key=len)
    # if len(strings) == 0:
    #     return None
    # return strings[0]
    # if len(strings) == 0:
    #     return None
    # elif len(strings) == 1:
    #     return strings[0]
    # else:
    #     for string in strings:
    #         if len(string) == len(strings[0]):
    #             return string
    #     return None

