Here's a self-contained Python script that defines a function filter_by_prefix that filters an input list of strings based on their prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

The function uses the starts-with operator to check if each string in the list starts with the given prefix. It then returns a string in a new list.

Let's take the input list: ['abc', 'bcd', 'cde', 'array'] and the prefix 'a':
```python
[abc, 'array']
```

This list will be returned by the function.