```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Out of list of strings, return the longest one.
    """
    longest = str()

    # Check for empty list
    if not strings:
        return None

    # Find the length of each string and find the longest one
    for string in strings:
        if len(string) > len(longest):
            longest = string

    return longest

# Test the function
text = ['a', 'b', 'c']
print(longest(text))  # Output: 'a'
```