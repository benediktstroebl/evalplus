Here is a Python script with a self-contained function that solves the problem of filtering strings for a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```

This script provides a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list containing only the strings that contain the substring. 

The function uses a list comprehension to iterate over the input list and a boolean condition to check if each string contains the substring. 

The test cases demonstrate how the function works, passing the expected output for the given inputs.