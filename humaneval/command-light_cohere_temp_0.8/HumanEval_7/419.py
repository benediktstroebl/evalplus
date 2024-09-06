```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```

This code defines a function called `filter_by_substring`, which takes a list of strings and a substring as input and returns a new list of strings that contain the substring. The function uses the Python's `contains` method to check if each string in the list contains the substring.