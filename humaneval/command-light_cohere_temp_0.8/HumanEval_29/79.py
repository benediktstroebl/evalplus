```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

The provided Python script defines a function named `filter_by_prefix` that filters an input list of strings based on their prefixes. The function uses the filtering logic where it iterates over the input strings and compares each one with the given `prefix`. The resulting filtered list contains only those strings that start with the specified prefix.