Here's the Python code that solves the problem of filtering strings starting with a given prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This script defines a `filter_by_prefix` function that takes a list of strings and a prefix as input and returns a new list containing only the strings from the input list that start with the given prefix. The function uses the expected to successfully filter the input strings.