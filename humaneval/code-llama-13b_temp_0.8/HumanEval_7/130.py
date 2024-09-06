from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [string for string in strings if substring in string]


    {"name": "Intro to Python", "attendees": 34},
    {"name": "Learn about Development", "attendees": 88},
    {"name": "Speaking publicly at a Meetup", "attendees": 10},
    {"name": "Intro to R", "attendees": 43},
    {"name": "Python for Beginners", "attendees": 6},
