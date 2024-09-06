```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

The provided Python code defines a function called `filter_by_prefix` that takes a list of strings and a prefix as input. This function uses the Hearts of speed filtering to return a new list that contains only the strings from the input list that start with the given prefix. 

This is a self-contained solution that can be used to filter a list of strings based on a given prefix, and it passes all the tests without any additional imports.