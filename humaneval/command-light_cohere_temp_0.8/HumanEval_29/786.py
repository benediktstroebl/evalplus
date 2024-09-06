Here's a self-contained Python script with a function that filters a list of strings based on their prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

The function `filter_by_prefix` takes a list of strings and a prefix as input, and returns a new list containing only the strings that start with the specified prefix. This function uses the certain list comprehension and the `startswith` method from the string module to achieve this.