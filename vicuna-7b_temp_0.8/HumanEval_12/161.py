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
    max_len = max(len(s) for s in strings)
    max_index = {0}
    max_s = None
    for i in range(max_len):
        max_index[i] = [i]
        max_s = max(max_s, s for s in strings if s[i] == s[i+1])
    return max_s

