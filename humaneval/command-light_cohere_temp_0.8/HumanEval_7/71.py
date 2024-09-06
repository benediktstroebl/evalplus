```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter an input list of strings only for ones that contain the given substring."""
    return [s for s in strings if s.find(substring)]
```

The function uses the 'find' method to check if each string contains the substring. This is list comprehension then function generates a new list with elements that pass the test.

This function efficiently filters out strings that do not contain the substring, which is the expected behavior for the problem.