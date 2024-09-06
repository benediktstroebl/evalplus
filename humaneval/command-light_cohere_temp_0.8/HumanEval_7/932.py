Here is a Python script with a self-contained function that solves the problem of filtering an input list of strings for ones that contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This script defines a function `filter_by_substring` that filters a list of strings for ones that contain a given substring. The function uses a list comprehension to iterate over the input strings and returns only those that contain the specified substring. 

This function is fully self-contained and does not require any external modules or functions.