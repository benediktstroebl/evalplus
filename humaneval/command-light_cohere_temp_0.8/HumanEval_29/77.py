```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

The provided Python script defines a function called `filter_by_prefix` that takes a list of strings and a prefix as input. It uses the Lisp (List comprehension) with the `startswith` method to filter and return the strings that start with the given prefix.