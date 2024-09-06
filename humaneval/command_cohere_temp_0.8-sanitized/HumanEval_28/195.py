from typing import List
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    # Check if the input list is empty
    if not strings:
        return ''
    
    # Use a join() method to concatenate strings in the list
    return ''.join(strings)