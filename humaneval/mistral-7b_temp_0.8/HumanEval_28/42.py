from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    assert type(strings) == list
    assert all(isinstance(string, str) for string in strings)
    return ''.join(strings)

