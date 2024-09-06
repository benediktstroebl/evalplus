Here is a self-contained Python script that defines a function `filter_by_substring` that filters an input list of strings based on whether the strings contain a given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]
# Test the function with various inputs and expected outputs
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"

# First Test: empty list
result = filter_by_substring(strings, substring)
print("First Test - Result:", result)

# Second Test: one substring present in strings
result = filter_by_substring(strings, "abc")
print("Second Test - Result:", result)

# Third Test: substring not present in strings
result = filter_by_substring(strings, "def")
print("Third Test - Result:", result)
```
This script provides a function to filter a list of strings based on whether a given substring exists in each string, with comprehensive tests to validate the function's behavior.