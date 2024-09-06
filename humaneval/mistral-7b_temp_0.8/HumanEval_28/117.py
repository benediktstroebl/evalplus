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
    if len(strings) == 1:
        return strings[0]
    return strings[0] + concatenate(strings[1:])

