Here is a self-contained Python script with a function that filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

The function uses a list comprehension to filter the strings based on whether their prefix matches the given prefix.