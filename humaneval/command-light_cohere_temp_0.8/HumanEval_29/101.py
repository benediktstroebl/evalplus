```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [string for string in strings if string.startswith(prefix)]
```
This script defines a Python function `filter_by_prefix` that filters an input list of strings to remove any strings that do not start with a given `prefix`.  It uses the `startswith` method to check if each string in the list starts with the given prefix.