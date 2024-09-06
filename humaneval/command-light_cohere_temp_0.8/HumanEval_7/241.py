```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```
This Python function, `filter_by_substring`, takes a list of strings and a substring as input and returns a new list containing only the strings from the input list that contain the given substring. The function utilizes the `contains` to check if each string in the input list contains the given substring, effectively filtering the list based on the substring.