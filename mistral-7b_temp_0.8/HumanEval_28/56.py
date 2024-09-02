from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """

    # If the input is an empty list, return an empty string
    if not strings:
        return ""

    # Convert the list of strings to a string
    return ''.join(strings)

