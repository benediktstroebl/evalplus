from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    concatenated_strings = ""
    for string in strings:
        concatenated_strings += string
    return concatenated_strings


    'author': 'jt',
    'dataset': 'test'

