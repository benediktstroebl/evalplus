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
    def _longest(strings: List[str], acc: Optional[str]) -> Optional[str]:
        if strings:
            if acc is None:
                return _longest(strings[1:], strings[0])
            else:
                return max(acc, _longest(strings[1:], strings[0]), key=len)
        return acc

    return _longest(strings, None)

