```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script defines a function `filter_by_substring` that filters a list of strings, returning only the elements that contain a given substring. It uses the `contains` for checking for the substring in each string and returns the result as a new list.