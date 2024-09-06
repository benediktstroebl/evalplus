```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

The above Python script defines a function called `filter_by_prefix` that takes in a list of strings and a prefix as input parameters. The function then uses the type hint of `List[str]` for the `strings` parameter, which is a list of strings. It then creates a list comprehension that filters the strings in the list and returns only those that start with the given prefix.