from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)


    'name': 'Concatenation',
    'author': 'Anonymous',
    'description': 'Concatenates list of strings into a single string',
    'url': 'https://cses.fi/problemset/task/1070',
    'tags': ['strings']
