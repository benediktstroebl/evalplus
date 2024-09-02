from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    result = ""
    for word in strings:
        result += word
    return result


    'name': 'Concatenate',
    'author': 'Neko349
