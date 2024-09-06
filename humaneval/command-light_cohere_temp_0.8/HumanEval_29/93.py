```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This Python code defines a function `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list containing only the strings from the input list that start with the specified prefix. The code uses the core Python list comprehension technique to achieve this.