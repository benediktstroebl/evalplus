from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    if len(strings) == 0:
        return []
    elif len(strings) == 1:
        return strings
    else:
        return filter_by_substring(
            filter(lambda x: substring in x, strings[1:]),
            substring,
        )

