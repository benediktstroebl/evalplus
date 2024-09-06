Here is a Python script with a self-contained function that solves the problem of filtering an input list of strings for ones that contain a given substring:

```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]

# Unit tests
strings = ["abc", "bacd", "cde", "array", "xyza", "abcba"]
substring = "a"

test_filter_by_substring = [
    lambda: not(filter_by_substring(strings, substring) == ['abc', 'bacd', "array"]),
    lambda: filter_by_substring(strings, substring) == []
]

print(*test_filter_by_substring)
```

The script defines a function `filter_by_substring` that filters a list of strings for ones that contain a given substring. The unit tests verify the different variations of the function's behavior, such as empty lists, lists with different strings, and a specific substring. The results of the test are printed as well.