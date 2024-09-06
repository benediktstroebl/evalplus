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

    max_length = 0
    max_strings = []
    for string in strings:
        if len(string) == max_length:
            max_strings.append(string)
        elif len(string) > max_length:
            max_strings.clear()
            max_strings.append(string)
            max_length = len(string)

    return max_strings[0]

