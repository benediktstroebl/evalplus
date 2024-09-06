Here's a solution:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function uses a list comprehension to filter out the strings from the input list that have the given prefix. It does not rely on any external modules or functions and is fully self-contained.