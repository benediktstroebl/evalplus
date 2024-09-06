Here's a self-contained Python script that provides the solution to filter out strings starting with a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function **filter_by_prefix**, which takes a list of strings and a prefix as input. It then creates a filtered list that contains only the strings that start with the given prefix. This is a simple and efficient way to solve this problem.