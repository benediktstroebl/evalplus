from typing import List
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    # If the input list is empty, return an empty string
    if not strings:
        return ''
    
    # Use join() to concatenate the strings in the list with spaces
    return ' '.join(strings)