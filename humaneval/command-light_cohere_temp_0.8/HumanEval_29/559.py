```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This Python code defines a function called `filter_by_prefix` that filters an input list of strings based on whether they start with a given prefix. 

It utilizes the `startswith` method to check if each string in the list starts with the specified prefix.