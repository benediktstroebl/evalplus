```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This Python script defines a function `filter_by_prefix` that filters a list of strings based on whether the string starts with a given prefix. 

It uses the `startswith` method of string to check the prefix match.