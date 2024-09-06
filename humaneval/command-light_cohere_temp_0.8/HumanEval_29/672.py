```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This Python function, `filter_by_prefix`, takes a list of strings and a prefix as input and returns a new list containing only the strings that start with that given prefix. 

This function uses the list comprehension with the `startswith` method to achieve this.