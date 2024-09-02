from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """

    # If the prefix is '', we don't need to filter anything
    if prefix == '':
        return strings

    # Filter the list based on the prefix
    filtered_list = list(filter(lambda x: x.startswith(prefix), strings))

    return filtered_list

