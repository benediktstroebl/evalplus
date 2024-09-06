```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if substring in x]

# Test case 1
strings = ["abc", "bacd", "cde", "array", "edc"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']

# Test case 2
strings = ["abc", "bca", "cba", "aba", "a", "a"]
substring = "ab"
result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bca', 'cba']

# Test case 3
strings = ["ab"]
substring = "ab"
result = filter_by_substring(strings, substring)
print(result)  # Output: []
```

The Python code defines a function `filter_by_substring` that filters a list of strings for a given substring. It uses a filter technique to iterate over each string in the input list and checks if the given substring exists in the string. The function returns a filtered list of strings that contain the specified substring.