```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This Python function uses the starts-with operator to filter an input list of strings, only keeping those that start with the specified prefix. It is tested with the list of strings and a prefix string, and returns a new list containing only the strings that start with that prefix.