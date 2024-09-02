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
    string_lengths: List[int] = []
    for string in strings:
        if len(string) > 0:
            string_lengths.append(len(string))
    if len(string_lengths) == 0:
        return None
    return strings[string_lengths.index(max(string_lengths))]

