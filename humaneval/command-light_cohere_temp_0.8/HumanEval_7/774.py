```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases for function
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"

results = filter_by_substring(strings, substring)
print(results)  # Output: ['abc', 'bacd', 'array']
```

This Python code defines a function `filter_by_substring` that filters a list of strings based on a given substring. The function iterates through each character in the input list to check if it contains the given substring. 

This approach is self-contained and does not rely on any external modules or functions.