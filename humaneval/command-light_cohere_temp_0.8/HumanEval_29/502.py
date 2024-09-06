```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function uses a list of strings and a prefix to filter and return only the strings that start with that prefix. The function uses the string.s for each test elements that match the prefix condition.