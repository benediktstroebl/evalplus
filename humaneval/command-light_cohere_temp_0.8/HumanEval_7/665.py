Here is a self-contained Python script that defines a function `filter_by_substring` that solves the problem you described:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.find(substring) != - None]
```

This script provides a function that filters an input list of strings, returning only those that contain the given substring. The function utilizes the-like x in strings if x.find(substring) != None, None is false if the substring is not found, so the function returns the list of strings that contain the substring.