Here is a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list containing only the strings from the input list that start with the given prefix. 

The function uses the `startswith` method to check if each string in the input list starts with the given prefix.