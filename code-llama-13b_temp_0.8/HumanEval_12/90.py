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
    if strings == []:
        return None
    max_len = 0
    for s in strings:
        if len(s) > max_len:
            max_len = len(s)
            longest_str = s
    return longest_str

    # Another, not working solution
    # if strings == []:
    #     return None
    #
    # max_len = 0
    # longest_str = None
    # for s in strings:
    #     if len(s) > max_len:
    #         max_len = len(s)
    #         longest_str = s
    # return longest_str
