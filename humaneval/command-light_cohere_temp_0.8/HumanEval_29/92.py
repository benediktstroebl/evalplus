Here is a Python script with a self-contained function that solves the problem of filtering strings based on a prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

The function uses a list comprehension with the `startswith` method to filter the strings based on the given prefix. 

It tests if the prefix starts with the given string, if it does, then it returns that string.