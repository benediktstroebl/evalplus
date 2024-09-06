```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test cases
strings = ["abc", "hello", "world"]
substring = "lo"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['hello']

strings = ["abc", "bacd", "cde", "array", "hello"]
substring = "d"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['cde', 'bacd']
``` 

This Python code defines a function `filter_by_substring` that filters a list of strings based on whether the given substring exists within each string. It then applies this filter to test cases: it creates a list of strings and a substring. Finally, it prints the expected output, which is the strings that contain the given substring.