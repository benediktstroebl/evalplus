```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This Python code defines a function `filter_by_prefix` that takes a list of strings and a prefix as input. It uses the particular character called a generator expression to filter the strings in the list, only keeping those that start with the given prefix.