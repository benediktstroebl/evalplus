Certainly! Here is a Python script with a self-contained function that solves the problem of filtering strings based on a prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings and a prefix as input and returns a new list that contains only the strings that start with the given prefix. It uses the testing's `startswith` method to check if each string starts with the given prefix.