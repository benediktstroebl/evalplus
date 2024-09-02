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
    max_len = len(max(strings, key=lambda s: len(s)))
    for i in range(max_len):
        for string in strings:
            if len(string) < max_len:
                continue
            if string[i]!= string[i + 1]:
                return string[:i]

