```python
from typing import List
def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python function filters a list of strings, returning a new list containing only those strings that contain a given substring. The function uses the Python's in-built contains() method to check if each string contains the given substring.