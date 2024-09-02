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
    # Combine the first element with the rest
    return ''.join(strings[0] + concatenate(strings[1:]))

