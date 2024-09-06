```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```
This script defines a function called `filter_by_substring` that filters an input list of strings and returns a new list that contains only the strings that contain the given substring. The function uses the process and returns a testable list to ensure the function is working correctly.