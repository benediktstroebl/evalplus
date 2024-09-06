from typing import List
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    # Checking if the input list is empty
    if not strings:
        return ''
    
    # Using concatenation operator to combine strings in the list
    return ''.join(strings)