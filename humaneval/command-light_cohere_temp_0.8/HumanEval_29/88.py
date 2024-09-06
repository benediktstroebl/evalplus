Here is a Python script that contains a self-contained function that filters an input list of strings based on a prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

The function uses a list comprehension to filter the strings in the input list. The function tests a test cases and passes. It is an good way of filtering strings with a given prefix.

It is a self-contained function that is easy to understand and does not rely on any external libraries.