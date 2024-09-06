from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    string = ''

    for i, string in enumerate(strings):
        if i == 0:
            string = string
        else:
            string += string

    return string

