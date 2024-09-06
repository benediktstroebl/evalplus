Here is a self-contained Python script with a function that filters an input list of strings for those containing a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This script defines a function that takes in a list of strings and a substring, and returns a new list that contains only the strings from the input list that contain the given substring.