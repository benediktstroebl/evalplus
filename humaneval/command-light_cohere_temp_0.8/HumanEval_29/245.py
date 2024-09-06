```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function uses the starts-with operator to filter the strings in the list that have the given prefix. It returns a general list of the strings that start with the given prefix.