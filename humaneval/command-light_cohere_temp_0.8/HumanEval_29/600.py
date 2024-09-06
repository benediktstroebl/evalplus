```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This Python code defines a function called `filter_by_prefix`, which filters a list of strings based on whether their prefix matches a given prefix. The function uses the strings and prefix as input parameters, and returns a new list containing only the strings that start with the given prefix.