Here is a Python script that contains a self-contained function that solves the problem of filtering strings based on a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This function iterates through the list of strings and returns a new list containing only the strings that contain the given substring.