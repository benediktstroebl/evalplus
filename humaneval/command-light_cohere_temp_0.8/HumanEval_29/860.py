Here is a Python script with a self-contained function that solves the problem of filtering strings based on a prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This script provides a function `filter_by_prefix` that filters an input list of strings based on whether they start with the given prefix. The function uses the filtering by checking if each element in the string starts with the specified prefix.