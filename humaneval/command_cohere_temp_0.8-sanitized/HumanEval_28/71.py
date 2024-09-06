from typing import List
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    Empty list returns empty string.
    """
    result = ''.join(strings)
    return result