from typing import List
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    Empty lists result in an empty string.
    """
    result = ''.join(strings)
    return result