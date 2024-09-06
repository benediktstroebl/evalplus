Here is a Python script with a self-contained function that filters an input list of strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This script defines a function **filter_by_prefix** that takes in a list of strings and a prefix, and returns a new list that contains only the strings from the input list that start with the given prefix.