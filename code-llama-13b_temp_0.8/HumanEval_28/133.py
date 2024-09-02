from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    concatenated = strings[0]
    for i in range(1, len(strings)):
        concatenated += strings[i]
    return concatenated
