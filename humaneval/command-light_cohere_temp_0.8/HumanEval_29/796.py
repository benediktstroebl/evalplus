```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This script defines a `filter_by_prefix` function that filters an input list of strings based on their prefix. It uses the specific character called `startswith` which checks if the given string starts with the given prefix.