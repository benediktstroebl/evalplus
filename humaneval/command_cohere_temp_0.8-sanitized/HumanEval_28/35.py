from typing import List
def concatenate(strings: List[str]) -> str:
    """
    Concatenate all strings in the list into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    concatenated = ''.join(strings)
    return concatenated