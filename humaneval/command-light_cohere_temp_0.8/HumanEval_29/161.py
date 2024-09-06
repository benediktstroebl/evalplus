```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This Python code defines a function called `filter_by_prefix`, which takes a list of strings and a prefix as input and returns a new list containing only the strings that start with the given prefix. 

The code uses the list comprehension to filter out the strings that match the given prefix.