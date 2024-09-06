```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This Python script defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. It uses the `startswith` method to check if each string in the list starts with the given prefix.