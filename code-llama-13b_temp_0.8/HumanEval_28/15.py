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
    'example_input_variables': {
        'list_of_strings': ['a', 'b', 'c']
    },
    'example_output_variables': {
        'concatenated_strings': 'abc'
    },
    'input_variable_type_description': {
        'list_of_strings': '`list` of `str` elements',
    },
    'output_variable_type_description': {
        'concatenated_strings': '`str`',
    },
