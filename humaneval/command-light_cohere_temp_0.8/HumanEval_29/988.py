Here is a self-contained Python script that solves the problem of filtering an input list of strings based on a prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input and returns a new list of strings that start with the specified prefix. The function uses the array's list comprehension with a list of strings and the `startswith` method to filter the strings that start with the given prefix.