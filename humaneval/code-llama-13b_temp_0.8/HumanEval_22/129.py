from typing import List, Any


def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {}, []])
    [1, 2, 3]
    """
    return [value for value in values if isinstance(value, int)]


    'name': 'Filter integers',
    'author': 'Anonymous',
    'description': 'Filter given list of any python values only for integers',
    'documentation': 'https://github.com/codearms/belina',
    'input': [
        {
            'label': 'List of values',
            'type': 'list',
            'placeholder': 'List of values',
        }
    ],
    'output': [
        {
            'name': 'Filtered',
            'type': 'list',
            'description': 'Filtered values',
        }
    ]
