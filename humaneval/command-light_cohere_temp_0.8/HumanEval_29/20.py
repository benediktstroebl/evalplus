```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function **filter_by_prefix** that filters an input list of strings based on their prefix. The function uses the filtering where it checks if each string in the list starts with the given prefix. This function is a output is a new list containing only the strings that match the given prefix.