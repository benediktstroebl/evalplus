```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This Python script defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. The function uses the filtering technique to return only the strings that start with the specified prefix.