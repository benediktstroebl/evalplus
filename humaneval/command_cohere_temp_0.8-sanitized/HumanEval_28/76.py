from typing import List
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    # Iterating through the list of strings and adding them to a string variable
    result = ''
    for string in strings:
        result += string
    return result