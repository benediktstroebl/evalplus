```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```

This code implements a function **filter_by_substring** that filters an input list of strings and returns a new list containing only the strings that contain the given substring. The function uses the interesting typing and a concise for-loop implementation to solve this problem.