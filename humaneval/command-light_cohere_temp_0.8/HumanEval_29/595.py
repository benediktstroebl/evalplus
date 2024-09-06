```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function called **`filter_by_prefix`** that filters an input list of strings based on a given prefix. The function uses the Python's **`startswith`** method to check if each string starts with the given prefix.

The function returns a new list containing only the strings from the input list that start with the specified prefix.