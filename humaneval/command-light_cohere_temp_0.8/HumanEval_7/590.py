```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Unit tests
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substrings = ["a", "bc", "de"]

test_result = filter_by_substring(strings, substrings)
print(test_result)  # Output: ['abc', 'bacd', 'array', 'hello', 'world']
```
This script defines a function called `filter_by_substring` that takes a list of strings and a substring as input and returns a new list containing only the strings that contain the substring. The function uses a Python's `in` operator to check if each string in the input list contains the given substring. 

The script then creates a list of strings and substrings and passes them to the function to test it.