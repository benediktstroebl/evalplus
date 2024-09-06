```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

The code implements a function called `filter_by_prefix` that filters an input list of strings and returns only the ones that start with a given prefix. 

It uses the `startswith` method to filter the strings and returns the desired list.