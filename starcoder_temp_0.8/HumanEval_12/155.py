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
    if len(strings) == 1:
        return strings[0]

    def compare(a, b):
        if len(a) == len(b):
            return a < b
        return len(a) > len(b)

    strings.sort(key=functools.cmp_to_key(compare))
    return strings[0]
