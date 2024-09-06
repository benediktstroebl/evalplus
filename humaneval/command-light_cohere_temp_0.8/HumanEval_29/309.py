```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This Python code defines a function called `filter_by_prefix` that takes two parameters: a list of strings and a prefix. The function filters and returns a new list of strings that start with the given prefix from the input list.