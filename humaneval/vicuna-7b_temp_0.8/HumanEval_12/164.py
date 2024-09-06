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
    elif len(strings) == 1:
        return strings[0]
    else:
        max_length = max(len(s) for s in strings)
        for i in range(max_length):
            max_len_string = "".join([s[i] for s in strings])
            if len(max_len_string) > len(max_length_string):
                max_length_string = max_len_string
        return max_length_string

