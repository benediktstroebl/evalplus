```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    
    # Validate input
    if not strings:
        raise ValueError("Input cannot be empty")
    
    # Initialize a new string to store concatenation
    result = ""
    
    # Concatenate strings in a list
    for string in strings:
        if string:  
            result += string + " "
    
    # Remove extra spaces
    return result.
```