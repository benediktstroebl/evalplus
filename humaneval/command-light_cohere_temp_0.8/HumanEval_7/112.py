Here is a self-contained Python script that solves the problem of filtering strings that contain a given substring:
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if substring in s]

# Test cases
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"

result = filter_by_substring(strings, substring)
print(result)
```

The script defines a function `filter_by_substring` that takes two parameters - a list of strings and a substring. It returns a the filtered list of strings that contain the given substring. 

This function can be easily used with any list of strings and a desired substring to filter the list accordingly.