Here is a Python script that contains a self-contained function that solves the problem of filtering strings based on a prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list that contains only the strings from the input list that start with the specified prefix.