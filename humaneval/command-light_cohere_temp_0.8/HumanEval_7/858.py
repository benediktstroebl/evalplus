```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python script defines a function `filter_by_substring` that filters an input list of strings to only include those that contain a given substring. The function uses the Python's `contains` operator to check if each string in the input list contains the given substring.