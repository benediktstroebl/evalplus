from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


    {"id": "wsL0Md", "topic": "Intro to Python"},
    {"id": "tQAsnt", "topic": "Intro to JavaScript"},
    {"id": "qf8vw9", "topic": "Intro to Ruby"},
    {"id": "nzJ03h", "topic": "Intro to Java"},
    {"id": "udDci5", "topic": "Intro to C"},
    {"id": "mqEK2w", "topic": "Intro to C#"},
    {"id": "91vAap", "topic": "Intro to C++"},

