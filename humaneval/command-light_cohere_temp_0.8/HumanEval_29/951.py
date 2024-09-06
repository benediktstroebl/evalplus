Here is a self-contained Python script that defines a function filter_by_prefix, which solves the problem of filtering an input list of strings based on their prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This script provides a function that takes a list of strings and a prefix as input, and returns a new list that contains only the strings from the input list that start with the specified prefix. 

The function uses a list comprehension to iterate through the input strings and check if each string starts with the given prefix.