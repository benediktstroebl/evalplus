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

    result = strings[0]

    for string in strings[1:]:
        result += string

    return result

