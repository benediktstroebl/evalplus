Here is a Python script with a self-contained function that solves the problem of filtering strings by their prefixes and passes corresponding tests:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes a list of strings and a prefix as input, and returns a new list that contains only the strings from the input list that start with the given prefix.