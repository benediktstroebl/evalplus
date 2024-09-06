from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    prefix_index = strings.index(prefix)
    if prefix_index == -1:
        return []
    else:
        prefix_len = len(prefix)
        return [strings[i:i + prefix_len] for i in range(len(strings)) if i + prefix_len <= len(strings)]

