Here is a self-contained Python script that defines a function `filter_by_prefix`, which solves the problem you described:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function accepts a list of strings and a prefix as arguments, and it returns a new list that contains only the strings from the input list that start with the given prefix.