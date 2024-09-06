from typing import List
def concatenate(strings: List[str]) -> str:
    """
    Concatenate all strings in the list into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # If the list is empty, return an empty string
    if not strings:
        return ''
    # Otherwise, concatenate all strings in the list and return the combined result
    return ''.join(strings)