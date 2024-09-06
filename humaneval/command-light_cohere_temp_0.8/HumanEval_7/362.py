Here is a self-contained Python script that solves the problem you described:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "Hello"]
substring = "a"

print(filter_by_substring(strings, substring))  # Output: ['abc', 'bacd', 'array']

# Large list and large substring
strings = ["abcdefghijklmnopqrstuv"]
substring = "qrstuv"

print(filter_by_substring(strings, substring))  # Output: ['abcdefghijklmnopqrstuv"]
```

This script provides a function called `filter_by_substring` that takes a list of strings and a substring as input. The function filters the the strings in the list and returns a new list containing only the strings that contain the given substring. This function is testing is both simple and more complex cases, passing the corresponding tests successfully.