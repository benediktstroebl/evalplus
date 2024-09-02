from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """

    # First filter only for strings that have a prefix
    filtered_strings = [string for string in strings if string.startswith(prefix)]

    # Then filter only for strings that have the correct prefix
    # We use a lambda expression here, a filtering function of type `bool`
    return list(filter(lambda string: string.startswith(prefix), filtered_strings))

