Here is a self-contained Python function that filters an input list of strings for ones that contain a given substring:
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function uses the contains() method to check if each string in the input list contains the given substring. The function returns a filtered list of strings that contain the specified substring.