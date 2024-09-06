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
    assert strings is not None, "The input list is None"
    assert isinstance(strings, list), "The input is not a list"

    if len(strings) == 0:
        return None

    strings.sort(key=len, reverse=True)
    return strings[0]

