```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This code implements a function called `filter_by_prefix` that filters an input list of strings to only include those that start with a specific prefix. It uses the technique of iterating through list comprehension and the `startswith` method from the string module.