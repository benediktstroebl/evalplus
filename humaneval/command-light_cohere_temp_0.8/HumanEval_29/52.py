Here is a self-contained Python script that includes a function `filter_by_prefix` that filters an input list of strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This script provides a function that takes a list of strings and a prefix, and returns a new list that includes only the strings from the input list that start with the given prefix.