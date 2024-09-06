from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # initialize an empty string
    concat = ''
    # loop through each string in the list
    for s in strings:
        # concatenate the string with the existing string
        concat += s
    # return the string
    return concat

