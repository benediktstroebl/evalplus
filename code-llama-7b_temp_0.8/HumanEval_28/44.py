from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # concatenate = ''.join(strings)
    # return concatenate
    #
    # Alternative solution
    return strings[0] if len(strings) == 1 else strings[0] + concatenate(strings[1:])

