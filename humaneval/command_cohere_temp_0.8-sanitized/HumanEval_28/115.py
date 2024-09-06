from typing import List
def concatenate(strings: List[str]) -> str:
    """
    Concatenate all strings in the list and return the result as a single string.
    """
    result = ''.join(strings)
    return result
strings = ['a', 'b', 'c']