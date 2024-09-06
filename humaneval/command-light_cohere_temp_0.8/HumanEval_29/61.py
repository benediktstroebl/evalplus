```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function uses the `startswith` method to filter the strings in the input list that have the given prefix. It returns a list of the desired strings starting with the specified prefix.