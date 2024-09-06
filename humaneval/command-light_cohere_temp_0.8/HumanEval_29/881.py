```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This Python function, `filter_by_prefix`, takes a list of strings and a prefix as input. It then iterates through the of the strings, checking if each one starts with the provided prefix. The function returns a list containing only those strings that start with the given prefix. 

This function is self-contained and can be easily incorporated into any larger program. It is a simple problem of filtering strings by a prefix, and can be a building block for more complex string manipulation tasks.