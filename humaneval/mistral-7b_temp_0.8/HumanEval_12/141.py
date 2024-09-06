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
    if len(strings) == 0:
        return None

    max_length = max(len(s) for s in strings)

    max_length_strings = []
    for s in strings:
        if len(s) == max_length:
            max_length_strings.append(s)

    if len(max_length_strings) == 1:
        return max_length_strings[0]

    return max_length_strings[0]

