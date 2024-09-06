Here is a self-contained Python script that includes the function `filter_by_prefix` that solves the problem of filtering an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list that contains only the strings from the input list that start with the given prefix. The function uses the string `startswith` to check if a string starts with the given prefix.