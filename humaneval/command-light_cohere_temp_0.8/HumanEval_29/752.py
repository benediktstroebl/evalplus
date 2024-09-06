```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This Python code defines a function called **filter_by_prefix** that filters a list of strings based on whether each string starts with a specific prefix. The function uses the string slicing to achieve this, and the return value is a new list containing only the strings from the original list that start with the given prefix.