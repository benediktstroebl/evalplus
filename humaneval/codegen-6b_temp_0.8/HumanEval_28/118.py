from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    result = ''
    if len(strings) == 0:
        return ''
    elif len(strings) == 1:
        return strings[0]
    else:
        for i in range(len(strings) - 1):
            result += strings[i]
            result += strings[i + 1]
        return result

