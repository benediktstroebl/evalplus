Here is a self-contained Python function that filters a list of strings for those containing a given substring:
```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function creates a new list that contains only the strings from the input list that contain the given substring.