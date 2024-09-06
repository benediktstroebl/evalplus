from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    result = ""
    for index in range(len(strings)):
        if index == 0:
            result = strings[index]
        else:
            result += strings[index]
    return result

