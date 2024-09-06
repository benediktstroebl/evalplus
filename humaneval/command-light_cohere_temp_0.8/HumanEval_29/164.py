```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This Python code defines a function called `filter_by_prefix`, designed to filter an input list of strings and return a new list that includes elements that start with a given prefix. The function utilizes the specific type hints and returns results for the given input.