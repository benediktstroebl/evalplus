from typing import List
def concatenate(strings: List[str]) -> str:
    """
    Concatenate list of strings into a single string.
    """
    # Check if the input list is empty
    if not strings:
        return ""
    
    # Use concatenation and str() to convert to string
    # Using f-strings for clearer formatting
    return "".join(str(string) for string in strings)