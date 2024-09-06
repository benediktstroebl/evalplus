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
    if len(strings) == 1:
        return strings[0]
    max_len = max(len(s) for s in strings)
    max_len_strings = []
    [max_len_strings.append(s) for s in strings if len(s) == max_len]
    return max_len_strings[0]

