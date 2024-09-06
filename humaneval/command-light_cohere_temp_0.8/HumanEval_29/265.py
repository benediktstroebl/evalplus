```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This code implements a function called **filter_by_prefix** that takes in a list of strings and a prefix, then returns a new list containing only the strings from the input list that start with that prefix.

This is a simple and efficient way to filter strings in Python, and it's a common tool in data manipulation.