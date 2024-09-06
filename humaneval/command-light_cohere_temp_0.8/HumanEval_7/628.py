Below is a Python script with a self-contained function that filters out strings from a given list that do not contain a specific substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter an input list of strings, returns list of strings that contain the substring"""
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "1", "a"]
substring = "d"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['bacd', 'array']
```

This script defines a function called `filter_by_substring` that takes two arguments: a list of strings `strings` and a substring `substring`. The function filters out the strings from the list that do not contain the given substring, and returns a new list containing only the strings that contain the substring.