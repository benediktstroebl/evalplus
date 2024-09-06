from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """

    # return "".join(strings)
    return_string = ""
    for string in strings:
        return_string += string
    return return_string

