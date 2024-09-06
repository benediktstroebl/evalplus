Here's the solution:

```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

The function uses a generator expression with the `startswith` method to filter the strings in the list, only keeping those that start with the given prefix.