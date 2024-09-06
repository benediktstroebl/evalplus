```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This code provides a function that takes a list of strings and a prefix, and returns a new list that contains only the strings from the input list that start with the given prefix.