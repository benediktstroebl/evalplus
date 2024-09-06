Below is a self-contained Python script that implements the `filter_by_substring` function, which filters an input list of strings based on whether the strings contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"

result = filter_by_substring(strings, substring)
print(result)  # Output: ['abc', 'bacd', 'array']
```

The `filter_by_substring` function utilizes a list comprehension to iterate over the input list of strings. It then uses the main if condition to check if each string contains the given substring. The output is a list of strings that contain the substring.