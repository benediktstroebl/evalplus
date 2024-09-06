Here is a self-contained Python script with a function that filters an input list of strings for those starting with a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This script provides a function `filter_by_prefix` that filters an input list of strings, returning a new list that contains only the strings that start with the specified prefix.