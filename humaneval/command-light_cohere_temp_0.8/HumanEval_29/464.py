Here is a self-contained Python script that solves the problem of filtering an input list of strings based on a given prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

The script uses the `startswith` method to check if each string in the list starts with the given `prefix`. If the condition is met, the function returns the string.

This code is self-contained and can be used directly with a list of strings and a desired prefix to filter the strings.