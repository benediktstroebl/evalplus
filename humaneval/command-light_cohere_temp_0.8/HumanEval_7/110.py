```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python code defines a function called **filter_by_substring** that filters a list of strings based on whether each string contains a given substring.  The function uses the string and substring as parameters and returns a new list containing only the strings that contain the substring.