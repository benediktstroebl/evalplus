```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
The code defines a function `filter_by_prefix` that filters an input list of strings based on whether their prefix matches the given `prefix`. It uses the `startswith` method to check if each element in the list starts with the given prefix.

The function returns a new list containing only the elements from the original list that match the given prefix.