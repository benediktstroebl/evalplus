```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python function uses the contains() method to filter an input list of strings and return a new list that contains only those strings that contain the given substring. The function is self-contained and provides an efficient solution for the given problem statement.