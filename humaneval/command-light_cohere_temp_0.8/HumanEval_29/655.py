```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This script provides a function **filter_by_prefix** that filters an input list of strings based on whether the string starts with the given prefix.  It tests this strings with the specified prefix.