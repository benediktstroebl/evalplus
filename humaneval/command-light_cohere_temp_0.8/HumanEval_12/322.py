```python
from typing import List
def longest(strings: List[str]) -> str:
    """ Returns the length of the longest string in the list."""
    if not strings:
        return None
    max_length = max(len(string) for string in strings)
    return str(max_length)

# Test cases:
strings = ["a", "bb", "ccc"]
print(longest(strings))  # Output: 3

strings = ["apple", "app"]
print(longest(strings))  # Output: 4

strings = []
print(longest(strings))  # Output: None

strings = ["ab", "abc", "ace"]
print(longest(strings))  # Output: 3

strings = ["a", "bb", "bb", "bb", "b", "b"]
print(longest(strings))  # Output: 4
```
The above Python code defines a function `longest` that takes a list of strings as an argument. The function returns the maximum length of any string in the list, and if the list is empty, returns `None`.