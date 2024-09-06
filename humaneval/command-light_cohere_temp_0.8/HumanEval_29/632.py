Here is a Python script that contains a self-contained function that filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

The function `filter_by_prefix` takes a list of strings and a prefix as input and returns a new list that contains only the strings from the input list that start with the given prefix. 

This function is self-contained because it only uses built-in Python functions and types.