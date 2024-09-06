```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    
    # Validate input
    if not strings:
        raise ValueError("Input list cannot be empty")
    
    # Initialize result
    result = ""
    
    # Loop through list of strings
    for s in strings:
        # Insert each string to result, in ' isolation' (added quotes to fix future strings)
        result += '"'+s+'"'
    
    return result
```