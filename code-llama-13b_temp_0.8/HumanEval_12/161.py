from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    return max(strings, key=len) if strings else None


    'name': 'Longest',
    'author': 'Anonymous',
    'description': 'Returns the longest string in a list.',
    'url': 'https://exercism.io/tracks/python/exercises/longest',
    'max_difficulty': 1,
    'has_code_snippets': False,
    'inherit_additional_args_from_exercise': False,
    'additional_args': [
        {
            'name': 'strings',
            'description': 'List of strings.',
            'type': 'list',
            'default': ['a', 'b', 'c'],
        },
    ],
