from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # hint: keep adding chars to the start of the result!
    result = ''
    for i in range(len(strings)):
        result = strings[i] + result
    return result

