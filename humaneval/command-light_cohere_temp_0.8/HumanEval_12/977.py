```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one.

    # Validate input
    string list
    if not strings:
        return None
    # Initialize variables
    max_length = 0
    longest_str = ""

    # Loop through strings
    for str in strings:
        # Find length of current string
        length = len(str)
        # Update max_length if current string is longer
        if length > max_length:
            max_length = length
        # Update longest string if needed
        if length > longest_str:
            longest_str = str

    return longest_str

# Example usage
# Test the function with sample inputs
strings = ["a", "b", "c"]
result = longest(strings)
print(result)  # Output: c
```
This code provides a self-contained solution to the problem.