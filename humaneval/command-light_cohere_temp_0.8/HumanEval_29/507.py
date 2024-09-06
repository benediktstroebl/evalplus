Here's a self-contained Python script with a function that filters an input list of strings for those starting with a given prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function is designed to take a list of strings and a prefix as input. It uses the `startswith` method to filter and return only the strings that start with the given prefix.