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

    # Index of the longest string
    idx_max = 0

    # The longest string
    max_str = strings[0]

    # Loop over the string in the list and find the longest
    for idx in range(1, len(strings)):
        if len(strings[idx]) > len(max_str):
            idx_max = idx
            max_str = strings[idx]

    return max_str

