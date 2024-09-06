Here is a self-contained Python script that solves the problem of filtering an input list of strings that starts with a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
The `filter_by_prefix` function uses a list comprehension to filter out any strings from the input list that start with the given prefix. It takes a string `startswith` method to compare the strings. The function returns a list of filtered strings.