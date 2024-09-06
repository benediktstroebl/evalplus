```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function called **`filter_by_prefix`** that filters an input list of strings, returning only those that start with the given prefix. It utilizes the `startswith` method from Python strings module to achieve this.

The function takes two parameters: 
- **`strings:`** This parameter represents the input list of strings.
- **`prefix:`** This represents the prefix string that the function should search for in each string.