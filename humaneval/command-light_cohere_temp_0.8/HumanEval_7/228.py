Here is a self-contained Python script that solves the problem of filtering an input list of strings that contain a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

The function uses the contains() method from string objects to check if each string in the list contains the given substring. The function returns a filtered list of strings.