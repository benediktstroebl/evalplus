from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    # begin the list with an empty one
    filtered_strings = []
    # check the input list
    for item in strings:
        # if the item starts with the input prefix, append it to the filtered list
        if item.startswith(prefix):
            filtered_strings.append(item)
    # return the list of filtered strings
    return filtered_strings


    'name': 'filter_by_prefix',
    'qparams': ['prefix']
