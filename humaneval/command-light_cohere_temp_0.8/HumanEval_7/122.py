```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases for function
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```
This Python script provides a function `filter_by_substring` that filters a list of strings based on a given substring. The test cases demonstrate the development of this function to solve the problem of filtering strings that contain a specific substring.