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
    'created_by': 'Jacob Smith',
    'classes': ['List'],
    'description': 'Concatenates a list of strings into a single string.',
    'source': 'https://github.com/camel-camel/camelCamel',

