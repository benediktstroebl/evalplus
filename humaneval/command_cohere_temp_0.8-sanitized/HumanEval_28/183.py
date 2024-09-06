from typing import List
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string
    """
    result = ''
    for string in strings:
        result += string
    return result