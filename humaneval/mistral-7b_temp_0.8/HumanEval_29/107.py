from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    def helper(strings, prefix):
        if len(strings) == 0:
            return []
        elif strings[0].startswith(prefix):
            return [strings[0]] + helper(strings[1:], prefix)
        else:
            return helper(strings[1:], prefix)
    return helper(strings, prefix)
