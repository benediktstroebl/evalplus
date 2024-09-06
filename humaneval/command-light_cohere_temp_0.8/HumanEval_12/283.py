Here's the solution:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string from the list.
    """
    # Check if list is empty
    if not strings:
        return None
    # Sort the list
    strings.sort()
   
    longest_str = strings[0]
    # Traverse the list and update the answer
    for string in strings[1:]:
        if len(string) > len(longest_str):
            longest_str = string
    return longest_str
```

Let me: a long list of strings. This code will return the longest string of the input list by finding the longest string from the list and returning it. It handles the empty list cases and performs the comparison using the `len` function to determine the length of each string.