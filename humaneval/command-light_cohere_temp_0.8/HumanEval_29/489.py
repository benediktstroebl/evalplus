```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function **filter_by_prefix** that filters a list of strings based on whether their prefixes match a given prefix.  It takes an function that uses the **startswith** method to check if each string starts with the given prefix.