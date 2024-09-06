```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]


# Test cases
strings = ["abc", "bacd", "cde", "array", "123", "hello"]
substring = "a"

# Function call with tests
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This script provides a function `filter_by_substring` that filters a list of strings based on a given substring. It uses a necessary list comprehension to iterate through the input strings and checks if each string contains the specified substring.