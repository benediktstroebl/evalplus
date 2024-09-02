from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # Empty string is base case
    if strings == []:
        return ''

    # Recursive case
    # Concatenate strings[1:] with strings[0]
    return strings[0] + concatenate(strings[1:])

