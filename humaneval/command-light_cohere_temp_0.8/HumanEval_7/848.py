```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This code defines a function **filter_by_substring** that takes a list of strings and a substring as input and returns a new list of strings that contain the given substring. The function uses the filter method to create the new list, which contains the elements of the original list that contain the given substring.