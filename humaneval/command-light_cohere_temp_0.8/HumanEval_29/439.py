```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function uses a list of strings and a prefix parameter to filter out all strings that do not start with the specified prefix. 

It then returns a new list that contains only the strings that match the given prefix.