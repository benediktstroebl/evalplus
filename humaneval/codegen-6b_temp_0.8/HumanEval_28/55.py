from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    concat = ""
    i = 0
    while i < len(strings):
        concat += strings[i]
        i += 1

    return concat

