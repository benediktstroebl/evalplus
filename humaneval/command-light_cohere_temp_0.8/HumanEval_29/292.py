Here's a self-contained Python script that defines a function `filter_by_prefix` that solves the problem of filtering an input list of strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This script provides a function that filters the input list of strings, removing any strings that do not start with the specified prefix. The output is a list of strings that start with the given prefix.