```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python function filters a list of strings, returning a new list containing only the strings that contain the given substring. The function uses the filter method, which returns all items that pass the filter condition.