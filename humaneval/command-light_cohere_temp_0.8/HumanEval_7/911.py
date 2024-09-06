```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python code defines a function called `filter_by_substring` that takes two parameters: a list of strings and a substring string. The function returns a filtered list of strings from the input list that contain the given substring.