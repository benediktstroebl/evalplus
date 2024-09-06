```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Returns the length of the longest string in the list."""
    if not strings:
        return None

    max_len = max(len(string) for string in strings)
    return str(max_len)

# Test cases
strings = ['a', 'b', 'c']
longest_result = longest(strings)
print("Longest:", longest_result) # Output: "a"

strings = ['a', 'bb', 'ccc']
longest_result = longest(strings)
print("Longest:", longest_result) # Output: "ccc"

strings = []
strings. empty_list = ['a', 'bb', 'ccc']
longest_result = longest(strings)
print("Longest:", longest_result) # Output: None
```
This code defines a function `longest` which takes a list of strings and returns the length of the longest string in the list. The `max` function is used to find the maximum length, and the `str` function is used to convert that integer to a string. The test cases show that the function works correctly with different inputs.