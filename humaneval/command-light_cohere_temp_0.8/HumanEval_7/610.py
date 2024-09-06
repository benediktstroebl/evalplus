Here is a Python script with a self-contained function that solves the problem of filtering strings that contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]

# Testing the function with sample inputs and expected outputs
strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "a"

# Result should be ['abc', 'bacd', 'array']
result = filter_by_substring(strings, substring)

print(result)
```