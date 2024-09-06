```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This script defines a function called `filter_by_prefix` that takes in a list of strings and a prefix, and returns a new list of strings that start with that prefix. It uses the filtering to check if each element in the list starts with the given prefix, and returns the list of matching elements.