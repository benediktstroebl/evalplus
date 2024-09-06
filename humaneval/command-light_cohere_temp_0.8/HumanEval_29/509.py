```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This Python function uses a generator expression to filter a list of strings and returns a new list that includes only the elements that start with the specified prefix.