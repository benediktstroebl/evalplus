from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """

    # for loop
    filtered = []
    for string in strings:
        if substring in string:
            filtered.append(string)

    # list comprehension
    filtered = [string for string in strings if substring in string]

    # list comprehension with enumerate
    filtered = [string for idx, string in enumerate(strings) if substring in string]

    return filtered

