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
    # BEGIN
    if not strings:
        return None
    else:
        sorted_strings = sorted(strings, key=lambda x: len(x), reverse=True)
        return sorted_strings[0]
    # END

