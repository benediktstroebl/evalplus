Here is a self-contained Python script that solves the problem of filtering strings that contain a given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
# Test cases
strings = ["abc", "bacd", "cde", "array", "Hello", "World"]
substring = "a"
result = filter_by_substring(strings, substring)
print(result)
```

The code defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list of strings that contain the substring. It uses a detailed typing and uses the list comprehension to filter the strings based on whether the substring is present.