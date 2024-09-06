from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """

    # filter(lambda s: s.startswith(prefix), strings)
    # [s for s in strings if s.startswith(prefix)]
    # [s for s in strings if s[0] == prefix[0]]
    # [s for s in strings if s[0] in prefix]
    # [s for s in strings if s[0] in list(prefix)]
    # [s for s in strings if s[0] in set(prefix)]

    prefix_set = set(prefix)

    return [s for s in strings if s[0] in prefix_set]
