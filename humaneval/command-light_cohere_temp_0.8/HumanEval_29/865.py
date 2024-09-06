Here is a self-contained Python script that defines a function filter_by_prefix that filters an input list of strings based on a given prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function takes two parameters: a list of strings and a prefix. string filter to search for. It uses the particular list comprehension and the `startswith` method to filter the strings that match the given prefix.