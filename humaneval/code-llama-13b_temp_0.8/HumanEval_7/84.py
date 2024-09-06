from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


    {"id": 1, "title": "Intro to Python", "date": "2018-10-01"},
    {"id": 2, "title": "Intro to Django", "date": "2018-10-02"},
    {"id": 3, "title": "Intro to Flask", "date": "2018-10-03"},
