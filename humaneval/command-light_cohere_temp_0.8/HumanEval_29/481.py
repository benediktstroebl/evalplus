```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

The function uses a generator expression and the `startswith` method to filter the strings in the list, which matches the given prefix. The test is passed to ensure the function works correctly.