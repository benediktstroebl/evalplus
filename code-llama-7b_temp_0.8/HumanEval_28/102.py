from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    if len(strings) == 0:
        return ''
    elif len(strings) == 1:
        return strings[0]
    else:
        return concatenate(strings[:-1]) + strings[-1]
