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

    max_len = max([len(s) for s in strings])
    max_string = ''.join(str(s) for s in strings)

    # Try to use a list comprehension with a while loop to avoid creating a new string
    # for each iteration. This is much faster than concatenating strings in each iteration.
    for i in range(1, max_len + 1):
        new_string = ''.join(str(s) for s in strings if len(s) >= i)
        if len(new_string) > len(max_string):
            return new_string
    return max_string

