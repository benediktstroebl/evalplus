```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This Python function uses the starts-with operator to filter a list of strings and return a new list containing only the strings that start with the given prefix.