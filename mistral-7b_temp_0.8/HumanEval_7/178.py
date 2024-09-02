from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """

    def _filter_by_substring(strings: List[str], substring: str) -> List[str]:
        if not strings:
            return []
        return [s for s in strings if substring in s]

    return _filter_by_substring(strings, substring)
