```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Unit tests
strings = ["abc", "bacd", "cde", "array", "hello", "World"]
substring = "a"

# Function call and check
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This code defines a function `filter_by_substring` that filters a list of strings for a given substring. It uses a templates to create a concise and readable solution.

The function takes two parameters: a list of strings `strings` and a substring `substring`. It iterates over the input list and returns a new list containing only the strings that contain the given substring. The unit tests use the approach to test the function.