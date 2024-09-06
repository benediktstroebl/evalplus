Here's the solution:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This function filters an input list of strings and returns a new list containing only the strings that start with the given prefix. It uses the operator `ist` to filter the strings that start with the given prefix.