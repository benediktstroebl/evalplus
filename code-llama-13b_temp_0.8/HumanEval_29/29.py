from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """

    # This is a version of the code that will run in O(n) time, but that
    # requires two passes over the input list.
    #
    # prefix_strings = []
    # for string in strings:
    #     if string.startswith(prefix):
    #         prefix_strings.append(string)
    # return prefix_strings

    # This version does the same thing, but in one pass using a list
    # comprehension.
    return [string for string in strings if string.startswith(prefix)]

