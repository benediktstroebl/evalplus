```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This Python function, `filter_by_prefix`, takes a list of strings and a prefix as input. It uses the filtering technique to return only the strings that start with the given prefix from the input list.