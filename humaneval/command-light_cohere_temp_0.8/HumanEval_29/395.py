```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
The function `filter_by_prefix` filters an input list of strings, returning only the ones that start with the given prefix.