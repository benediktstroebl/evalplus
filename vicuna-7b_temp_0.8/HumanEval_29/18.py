from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    prefix_len = len(prefix)
    prefixed_strings = [strings[i:i+prefix_len] for i in range(len(strings)) if not prefix in strings[i:i+prefix_len]]
    return prefixed_strings

