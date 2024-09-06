```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This Python code defines a function `filter_by_substring` that filters an input list of strings to only include those that contain a given substring. The function uses the approach by iterating over each string in the list and checking whether the string contains the provided substring using the `contains` method.