Here is a self-contained Python script that solves the problem of filtering an input list of strings that start with a given prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

The function takes two parameters: a list of strings (strings) and a prefix (prefix). The function uses a list comprehension to filter the input list of strings, only keeping those that start with the given prefix.