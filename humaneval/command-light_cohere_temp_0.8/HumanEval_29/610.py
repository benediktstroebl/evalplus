```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This code implements a filter_by_prefix function that takes in a list of strings and a prefix, and returns a new list with all elements that start with that prefix. This code uses the bound typing features to make the function more readable and maintainable.