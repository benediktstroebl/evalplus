```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This code implements a function called **filter_by_prefix** that filters a list of strings, returning only the elements that start with the specified prefix.