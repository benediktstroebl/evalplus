```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. It uses the string starting to check if each string in the list starts with the given prefix, and then returns the string. 

This function can be used to filter any list of strings that start with a given prefix.