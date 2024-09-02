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
    max_len = max([len(s) for s in strings])
    max_idx = 0
    max_string = ''.join(str(c) for c in ''.join(strings).split())
    for i in range(1, max_len + 1):
        string = ''.join(str(c) for c in ''.join(strings).split())
        if len(string) == i:
            return None
        elif len(string) > i and len(max_string) > i and string > max_string:
            max_string = max_string[:-i]
            max_idx = i - len(max_string)
            max_len = max_len - i
    return max_string