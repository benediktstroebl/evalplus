```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    # Check if the list is empty
    if not strings:
        return None
    
    # Sort the strings alphabetically
    strings.sort()
    
    # Return the needed the longest string in the list
    longest_string = max(strings, key=len)
    
    return longest_string
```