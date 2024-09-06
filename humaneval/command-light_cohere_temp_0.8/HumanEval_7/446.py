Here's a self-contained Python script that defines a function filter_by_substring that filters a list of strings for a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This function utilizes the contains() method to check if each string in the input list contains the given substring. It returns a