```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This Python function uses a generator expression to filter a list of strings, returning only those that start with the specified prefix. It utilizes the tested with different input lists and prefixes to pass the corresponding tests.