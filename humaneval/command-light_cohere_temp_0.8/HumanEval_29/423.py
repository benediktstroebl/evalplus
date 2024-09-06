```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This code provides a function that filters an input list of strings, only keeping the ones that start with a given prefix.