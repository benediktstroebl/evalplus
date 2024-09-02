from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """

    # use reduce function to concatenate 2 strings
    return reduce(lambda a, b: a + b, strings, '')

