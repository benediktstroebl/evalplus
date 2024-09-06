Here is a Python script with a self-contained function that solves the problem you described:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input. It returns a all list of strings that start with the given prefix.