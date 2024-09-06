```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter an input list of strings only for ones that contain the substring"""
    return [s for s in strings if s.find(substring)]
```

This script provides a function that filters an input list of strings, returns a new list containing only the strings that contain the given substring. The script utilizes the string.  `find()` method to search for the substring within each string, and the `filter()` function returns the resulting list of strings that contain the substring.