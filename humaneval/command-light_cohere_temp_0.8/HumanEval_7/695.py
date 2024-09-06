```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This code uses the contains() method to check if each string in the list contains the substring. It then returns a string list containing only the strings that contain the given substring.