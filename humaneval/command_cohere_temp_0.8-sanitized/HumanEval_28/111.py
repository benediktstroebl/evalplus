from typing import List
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    Empty list results in an empty string.
    """
    result = ''.join(strings)
    return result