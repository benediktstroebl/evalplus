Here's a self-contained Python script that solves the problem of filtering strings based on a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script defines a function `filter_by_substring` that takes a list of strings and a substring as input and returns a new list of strings that contain the substring. The function uses the method `contains` to check if each element in the input list contains the given substring.