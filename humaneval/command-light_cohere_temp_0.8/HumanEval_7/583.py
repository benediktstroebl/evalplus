```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This function is designed to filter and return a list of strings from an input list that contain a given substring. It uses the specific to List[str] and substring to iterate through the list and return any elements that contain the substring. The function is self-contained and efficiently solves the problem.