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
    first_string = strings[0]
    rest_of_strings = strings[1:]
    return first_string + concatenate(rest_of_strings)

