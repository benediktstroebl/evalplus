from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """

    if len(prefix) == 0:
        return strings
    new_strings = []
    for string in strings:
        if string.startswith(prefix):
            new_strings.append(string)
    return new_strings
