```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This Python code defines a function called **filter_by_prefix** that filters a list of strings based on whether the string starts with a given prefix. 

To do this, it uses a list comprehension that checks if each string in the input list starts with the given prefix.