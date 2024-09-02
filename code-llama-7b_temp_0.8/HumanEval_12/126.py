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
    strings_len = [len(string) for string in strings]
    if len(strings_len) == 0:
        return None
    longest_str_idx = max(range(len(strings_len)), key=strings_len.__getitem__)
    return strings[longest_str_idx]

