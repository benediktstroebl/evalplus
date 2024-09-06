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
    'description': 'Concatenate list of strings into a single string',
    'examples': [
        {
            'data': [[]],
            'output': ''
        },
        {
            'data': [['a', 'b', 'c']],
            'output': 'abc'
        }
    ]
