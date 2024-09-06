Here is a Python script with a self-contained function that solves the problem of filtering an input list of strings for those that start with a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

The function uses a list comprehension to filter the input list of strings based on whether the string starts with the given prefix. The function then returns a filtered list of strings.