```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This Python function, `filter_by_prefix`, takes a list of strings and a prefix as input and returns a new list that includes only the strings from the input list that start with the given prefix. The function uses the essential list comprehension to achieve this. The `startswith` method is used to compare if each string in the input list starts with the given prefix.