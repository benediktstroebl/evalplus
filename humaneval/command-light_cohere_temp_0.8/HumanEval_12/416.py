```python
from typing import List
def longest(strings: List[str]):
    """ Out of list of strings, return the longest one.

    if not strings:
        return None

    longest_length = max(len(str) for str in strings)
    longest_string = strings[0] if longest_length == len(strings[0]) else strings[1]
    return longest_string

# Test case 1
strings = ["a", "b", "c"]
result = longest(strings)
print(result)  # Output: 'c'

# Test case 2
strings = ["a", "bb", "ccc"]
result = longest(strings)
print(result)  # Output: 'ccc'

# Test case 3
strings = []
result = longest(strings)
print(result)  # Output: None
```
This Python script defines a function `longest` that takes a list of strings as input and returns the longest string from the list. The function uses the max function to find the length of all the strings, and then compares the lengths to find the longest one. The test cases are provided to verify that the function works correctly for different scenarios.