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
    lengths = {}
    for string in strings:
        lengths[len(string)] = string if len(lengths) == 0 else max(
            [lengths[len(string)], string], key=len
        )
    return lengths.get(max(lengths.keys()))

