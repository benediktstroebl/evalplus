```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that filters an input list of strings, returning a new list that contains only the elements that start with the specified prefix. 

The function uses the typing module for type hints, which is used to provide additional context about the function's expected parameters and return values.