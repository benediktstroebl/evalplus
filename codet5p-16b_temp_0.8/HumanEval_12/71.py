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

    strings_len = [len(s) for s in strings]
    longest_string_index = strings_len.index(max(strings_len))
    return strings[longest_string_index]
