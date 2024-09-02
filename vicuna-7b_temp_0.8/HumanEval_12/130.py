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
    max_idx = 0
    max_str = None
    for i in range(max_len):
        str_idx = 0
        max_str_len = len(strings[0]) + 1
        max_str = strings[0][:max_str_len] if max_str_len > 0 else ''
        for j in range(len(strings)):
            if len(strings[j]) > max_str_len:
                max_str += strings[j][:max_str_len]
                str_idx = j
                max_str_len = len(max_str[:str_idx])
        if max_str != max_str_len and max_str != max_str[-1]:
            max_str = max_str[::-1] + max_str[:-1]
            max_str_len = len(max_str)
        if max_str == max_str_len:
            max_str = max_str.upper()
            max_idx = str_idx
    return max_str

