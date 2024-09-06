from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    if not isinstance(strings, list):
        raise TypeError(f'Expected list of strings, got {type(strings)}')
    if not isinstance(substring, str):
        raise TypeError(f'Expected string, got {type(substring)}')

    return [x for x in strings if substring in x
