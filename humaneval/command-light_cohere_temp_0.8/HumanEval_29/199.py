```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This code implements a function `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list containing only the elements that start with that prefix. 

It uses the list comprehension with the "startswith" method to filter the strings.