```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function **`filter_by_prefix`** that filters an input list of strings based on their prefix. It uses the Python's list comprehension technique with the **`startswith`** method to achieve this. The function returns a list of strings that start with the given prefix.