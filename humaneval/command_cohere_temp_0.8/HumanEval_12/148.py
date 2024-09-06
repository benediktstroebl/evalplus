Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    longest_string = max(strings, key=len)  # Get the longest string
    if len(set(strings)) == 1:  # If there's only one longest string, return the first one
        return longest_string[0]
    else:
        return longest_string
```
This code defines a function `longest` that takes a list of strings (`List[str]`) as input and returns the longest string from the list. If there are multiple longest strings, it returns the first one among them, and if the list is empty, it returns `None`. The `longest` function utilizes the `max` function with a custom key function to compare strings based on their length. It also checks if there's only one longest string and returns the first instance of it, and otherwise, it returns the actual longest string.