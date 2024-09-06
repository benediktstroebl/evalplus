Here is a Python script with a self-contained function that solves the problem of filtering an input list of strings for those starting with a given prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function uses a list comprehension to filter out the strings from the input list that start with the given prefix. It takes advantage of Python's `startswith` method, which is built-in and helps to quickly check if a string starts with another.