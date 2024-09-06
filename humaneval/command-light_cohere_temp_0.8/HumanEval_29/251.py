```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This Python function, `filter_by_prefix`, takes a list of strings and a prefix as input. It returns a filter the this list to only include strings that start with the given prefix.