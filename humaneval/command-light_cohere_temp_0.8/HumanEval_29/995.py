```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This Python function uses a generator expression and the `startswith` method to filter an input list of strings, passing them through tests to see if each string starts with a given prefix.