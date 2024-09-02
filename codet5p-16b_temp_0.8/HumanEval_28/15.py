from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """

    if not strings:
        return ''
    else:
        return concatenate([s for s in strings if s]) + strings[0]
    

