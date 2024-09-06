```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.
    if prefix != ' ':
        yield prefix
    for i, c in enumerate(string, 1):
        yield f"{i}-{c}" if c.isalpha() else break

    return []

# Testing the function
test_string = "abc"
test_result = all_prefixes(test_string)
print("Test string:", test_string)
print("Expected prefixes:", test_result)

# Test empty string
empty_string = ""
test_result = all_prefixes(empty_string)
print("Test empty string:", empty_string)
print("Expected prefixes:", test_result)

# Test list of strings
test_list = ["abc", "aab", "123"]
test_result = all_prefixes(test_list)
print("Test list:", test_list)
print("Expected prefixes:", test_result)

# Test empty list
test_empty = []
test_result = all_prefixes(test_empty)
print("Test empty list:", test_empty)
print("Expected prefixes:", test_result)
```
This code provides a function `all_prefixes` that returns a list of all prefixes in a string, it then provides tests for the function with different inputs.