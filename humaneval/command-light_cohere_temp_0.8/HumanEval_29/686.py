Here's a self-contained Python script with a function that filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This script provides a function 'filter_by_prefix' that filters an input list of strings based on whether the string starts with a given prefix.