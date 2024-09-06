```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This Python code defines a function called **filter_by_prefix** that takes a list of strings and a prefix as input. The function uses the string prefix matching to return a new list that contains only the elements of the original list that start with the given prefix.