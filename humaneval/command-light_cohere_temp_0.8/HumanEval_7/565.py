```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```
The code defines a function called `filter_by_substring` that takes in two parameters: a list of strings and a substring string. It uses the does a list comprehension to filter the list of strings and returns a new list that contains only the strings that contain the given substring.