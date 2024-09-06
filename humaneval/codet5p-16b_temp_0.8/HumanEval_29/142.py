from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """

    if not strings:
        return []
    elif strings[0].startswith(prefix):
        return [strings[0]] + filter_by_prefix(strings[1:], prefix)
    else:
        return filter_by_prefix(strings[1:], prefix)
    
    
