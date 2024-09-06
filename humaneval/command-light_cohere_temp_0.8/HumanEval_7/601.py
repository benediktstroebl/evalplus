Here's the self-contained Python script that solves the problem of filtering an input list of strings that contain the given substring:
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if substring in string]
```

This script defines a `filter_by_substring` function that takes a list of strings and a substring as input and returns a new list of strings that contain the substring. The `List` function creates an empty list and then iterates over the input list, using the `in` operator, which checks if each string contains the given substring.