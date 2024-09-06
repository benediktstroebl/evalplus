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

The `filter_by_substring` function takes a list of strings and a substring as input and returns a new list containing only the strings from the input list that contain the given substring. 


The test cases demonstrate how the function works with different inputs and the expected outputs.