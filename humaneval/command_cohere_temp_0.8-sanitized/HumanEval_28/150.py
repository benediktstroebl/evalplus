from typing import List
def concatenate(strings: List[str]) -> str:
    # If the input list is empty, return an empty string
    if not strings:
        return ''
    
    # Use join() to concatenate the strings in the list with spaces and return the combined string
    return ' '.join(strings)