```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function employs a list comprehension and the startsswith() method to filter the input list of strings, only retaining those that commence with the specified prefix.