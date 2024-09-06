```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This function, `filter_by_prefix`, takes a list of strings and a prefix as input. It then creates a list of all strings that start with the given prefix, as indicated by the `startswith` method. 

The function effectively filters out all strings from the input list that do not start with the given prefix.