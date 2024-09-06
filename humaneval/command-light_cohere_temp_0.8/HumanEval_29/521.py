```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This code defines a function `filter_by_prefix` which takes a list of strings and a prefix as input, and returns a new list of strings that start with the given prefix. The function uses the majorly the list comprehension to achieve this, filtering out all strings from the input list that do not start with the given prefix.