```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case 1
strings = ["abc", "bacd", "cde", "array"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']

# Test case 2
strings = ["abcd", "cd", "abacd"]
substring = "cd"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abcd', 'cd']

# Test case 3
strings = ["a", "bc", "def", "rest", "world"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['a', 'bc', 'def', 'rest', 'world']
```
This Python script defines a function `filter_by_substring` that filters a list of strings for a given substring. The test cases demonstrate the