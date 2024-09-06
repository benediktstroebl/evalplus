from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # If the input list is empty, returning an empty string
    if not strings:
        return ''
    # Returning concatenated string by joining strings in the list with a space
    return ' '.join(strings)