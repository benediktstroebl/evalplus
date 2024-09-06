```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the longest string from the list of strings.
    """
    maximum = ""
    for s in strings:
        if len(s) > len(maximum):
            maximum = s
    return maximum
# Example usage
strings = ["a", "bb", "ccc"]
print(longest(strings))  # Output: "ccc"
``` 
This solution provides a self-contained function that accepts a list of strings and returns the longest string from the list. It utilizes a maximum approach to identify the longest string, which is the one with the longest length.