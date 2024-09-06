```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This Python script defines a function called **`filter_by_prefix`** that filters a list of strings based on whether their prefixes match a given prefix. It uses the general's a list of strings and a prefix as input. The function returns a list of strings that have the specified prefix.