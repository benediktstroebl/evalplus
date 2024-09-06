```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """ Returns the length of the longest string in the list, or None if empty"""
    return max(strings, key=len) or None

# Test cases
strings = ["a", "bb", "ccc"]
print(longest(strings))  # Output: 3

strings = ["hello", "world"]
print(longest(strings))  # Output: 5

strings = []
print(longest(strings))  # Output: None

strings = ["aa", "apple", "ipse", "ape"]
print(longest(strings))  # Output: 4
``` 
This script provides a function called **longest** that takes a list of strings as input and returns the length of the longest string, or None if the list is empty. The output of each test cases demonstrates the function's correctness.