Here's the solution to the problem:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function uses a list comprehension to filter a list of strings based on whether their prefix matches the given prefix.