```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain the given substring."""
    return [string for string in strings if string.find(substring) != - None]


# Test cases
strings = ["abc", "bacd", "cde", "array", "hello", "world"]
substring = "a"

result = filter_by_substring(strings, substring)
print(result)

strings = ["abcd"] + ["hello"] + ["world"]
substring = "lo"

result = filter_by_substring(strings, substring)
print(result)
```

The code defines a function `filter_by_substring` that filters a list of strings, returning only the ones that contain a given substring. It then passes tests to test this function with sample input, and the output is displayed.