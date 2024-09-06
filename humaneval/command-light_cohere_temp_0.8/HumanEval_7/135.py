```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The code defines a function that filters a list of strings, returning a new list that includes only the strings that contain the given substring. The function uses the test case in which it takes a list of strings and a substring as input and creates a new list with the strings that contain the substring.