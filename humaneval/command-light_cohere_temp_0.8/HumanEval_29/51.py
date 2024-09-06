Here's the solution to the problem you described:

```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function uses a list comprehension to filter the input list of strings based on whether their prefix matches the given prefix.