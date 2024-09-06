A Python function to filter an input list of strings based on their prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function uses the `startswith` method to check if each string in the list starts with the provided prefix. It returns a string in the list if the condition is true.

You can use this function to filter strings in a list that starts with a given prefix.