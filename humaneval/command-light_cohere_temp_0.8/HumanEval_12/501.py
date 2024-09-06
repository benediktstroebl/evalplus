```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string from a list.
    """
    # Check if list is empty
    if not strings:
        return None
    # Sort the strings
    strings.sort()
    unique sorted strings
   
    # Initialize the longest string
    longest = ""
    # Loop through the strings and append to longest
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest
```