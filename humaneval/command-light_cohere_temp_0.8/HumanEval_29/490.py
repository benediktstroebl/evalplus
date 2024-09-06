Here's a self-contained Python function that filters an input list of strings based on a given prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings and a prefix as input and returns a new list containing only the strings from the input list that start with the specified prefix. The `startswith` method is used to check if each string in the list starts with the given prefix.