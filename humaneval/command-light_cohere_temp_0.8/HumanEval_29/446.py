Here is a self-contained Python script with a function that filters an input list of strings based on a given prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

The `filter_by_prefix` function uses a list comprehension to filter the input list of strings based on whether the string starts with the given prefix.