Here is a Python script that contains a self-contained function that solves the problem of filtering an input list of strings that contain a given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script provides a function that filters and returns a new list containing only the strings from the input list that contain the given substring.