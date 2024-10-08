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
    elif len(strings) == 1:
        return strings[0]
    else:
        max_string = strings[0]
        for string in strings:
            if len(string) > len(max_string):
                max_string = string
        return max_string

