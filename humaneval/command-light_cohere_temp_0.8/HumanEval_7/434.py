Here is a Python script with a self-contained function that solves the problem of filtering strings that contain a given substring:

```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]

# Test the function
strings = ['abc', 'bacd', 'cde', 'array', 'hello world']
sub = 'a'
result = filter_by_substring(strings, sub)
print(result)
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list of strings that contain the given substring. The test code then creates a test list of strings and a substring, and passes them to the function. The function then returns a list of strings that contain the given substring, and the output is printed to the console.