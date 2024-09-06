Here's the solution:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This code employs the contains() method of strings to filter and create a new list containing strings that contain the given substring.