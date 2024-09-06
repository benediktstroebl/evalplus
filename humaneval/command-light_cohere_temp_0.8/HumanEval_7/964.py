Here's a self-contained Python function that filters a list of strings based on a given substring:
```python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [string for string in strings if string.contains(substring)]
```
The `contains` method checks if a string contains the `substring` using the `contains` function. The `filter` method then then applies this check on each string in the list.