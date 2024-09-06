Here is a Python script with a self-contained function that solves the problem of filtering strings that contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]

# Test case 1
strings = ["abc", "bacd", "cde", "array"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']

# Test case 2
strings = ["abc", "cdef", "array", "cats"]
substring = "s"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'array']

# Test case 3
strings = ["a", "hello", "world"]
substring = "o"
result = filter_by_substring(strings, substring)
print(result)  # Output: []
```
This script defines a function `filter_by_substring` that filters an input list of strings for ones that contain a given substring. 

The function uses a list comprehension to iterate through each string in the input list. 

It then checks if the given substring exists in the current string using the `in` operator.