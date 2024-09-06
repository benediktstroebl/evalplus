```python
from typing import List
def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string"""
    return ''.join(strings)

# Test cases
strings = ["a", "b", "c"]
result = concatenate(strings)
assert result == "abc"

# Test case with empty list
strings = []
result = concatenate(strings)
assert result == ''

# Test case with one string
strings = ["hello"]
result = concatenate(strings)
assert result == "hello"
```
This code defines a function `concatenate` that takes a list of strings as an argument and returns the concatenated string. It provides three list of test cases to cover all possible scenarios. It passes all test cases successfully.