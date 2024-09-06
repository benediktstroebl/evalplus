import string
def concatenate(strings: list) -> str:
    """
    Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    concatenated_string = string.join(strings)
    return concatenated_string