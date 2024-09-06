```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python function uses the contains() method to check if each string in the input list contains the given substring. The function then returns a list of all strings from the input list that contain the given substring.