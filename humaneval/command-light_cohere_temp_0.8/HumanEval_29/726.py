Here's a self-contained Python function that filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function takes a list of strings and a prefix as input, and returns a new list containing only the strings from the input list that start with the specified prefix. It uses the string.surring to check whether list comprehension to achieve this. The function is designed to be efficient, using a single loop and no additional data structures.