```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This Python script defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. It uses the string `startswith` to check if each element in the strings list starts with the given prefix. 

This function could be a great tool for many situations where you need to filter data based on a prefix.