Here is a Python script with a self-contained function that solves the problem and passes the corresponding tests:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

# Function call
result = filter_by_substring(strings, substring)

# Print results
print(result)  # Output: ['abc', 'bacd', 'array']
```
This code defines a function `filter_by_substring` that filters an input list of strings and returns a new list that contains only the strings that contain a given substring. The test cases demonstrate the fact that the function works correctly.