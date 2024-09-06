```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This Python code defines a function named **filter_by_prefix** that filters an input list of strings based on whether each string starts with a given prefix. It uses the filtered list comprehension to achieve this, and the result is a new list containing only the strings that start with the given prefix. 

This function is designed to be a self-contained way to filter strings based on their prefix.