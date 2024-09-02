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
    # pass
    if strings == []:
        return None
    elif len(strings) == 0:
        return None
    else:
        longest_str = strings[0]
        for i in range(len(strings)):
            if len(longest_str) < len(strings[i]):
                longest_str = strings[i]
            else:
                pass
        return longest_str
    # return longest_str

