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
    lengths = set([len(s) for s in strings])
    longest_s = None
    for length in lengths:
        for s in strings:
            if len(s) == length:
                if longest_s is None or len(s) > len(longest_s):
                    longest_s = s
                else:
                    pass
    return longest_s

