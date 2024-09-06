Here is a self-contained Python script that implements the filter_by_substring function from the previous prompt:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script defines a function that filters an input list of strings, returning a new list containing only the strings that contain the given substring.