```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
The function filters the input list of strings and returns a new list containing only the strings that start with the given prefix.