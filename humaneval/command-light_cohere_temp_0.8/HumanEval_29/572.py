Here's a self-contained Python function that filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings by their prefix."""
    return [x for x in strings if x.startswith(prefix)]
```
This function takes two arguments: a list of strings (`strings`) and a prefix (`prefix`). It uses the `startswith` method of the strings in the list to filter and return only the strings that start with the given prefix.