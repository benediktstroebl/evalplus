```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This Python code defines a function called `filter_by_substring` that takes a list of strings and a substring as input. The function uses the ** contains** operator to filter the list, only keeping the strings that contain the given substring.