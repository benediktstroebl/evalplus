```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python function filters an input list of strings and returns a new list containing only the strings that contain the given substring.  It string contains method is used to check if each string contains the substring.