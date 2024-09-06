```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substrings = ["a", "bd", "cde"]

expected = [('abc', 'bacd', "array"), ("hello",)

print(filter_by_substring(strings, substrings))
print(expected)
```

This Python code defines a function called `filter_by_substring` that filters an input list of strings based on whether the given substring exists within each string. The test cases verify that function's behavior, and the expected results are printed.