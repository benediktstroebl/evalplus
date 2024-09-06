```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings, keeping only those starting with the given prefix."""
    return [x for x in strings if x.startswith(prefix)]
```
This Python function uses the startsswith operator to filter a list of strings, keeping only those that start with a specified prefix. It does so by taking the list of strings and the prefix string as input and returning a new list with the filtered strings.