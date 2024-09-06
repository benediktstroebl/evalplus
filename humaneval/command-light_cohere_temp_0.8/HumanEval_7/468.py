Here is a Python script with a self-contained function that solves the problem of filtering an input list of strings that contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script defines a `filter_by_substring` function that takes a list of strings and a substring as input and returns a new list of strings that contain the substring. The function uses the `contains` which takes in a list of strings and a substring, and returns a new list of strings that contain the substring. This is process is fully self-contained and can be run independently, with no external dependencies.