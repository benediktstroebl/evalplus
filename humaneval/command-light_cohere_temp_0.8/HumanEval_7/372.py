```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
This code implements a `filter_by_substring` function that filters an input list of strings and returns only those that contain a given substring. 

It utilizes the `contains` to ensure type-checking, and the `contains` method to iterate over the list of strings.