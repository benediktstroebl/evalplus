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
    max_len: int = max(map(len, strings))
    longest_strings: List[str] = list(filter(lambda s: len(s) == max_len, strings))
    return longest_strings[0] if len(longest_strings) == 1 else strings[0]

