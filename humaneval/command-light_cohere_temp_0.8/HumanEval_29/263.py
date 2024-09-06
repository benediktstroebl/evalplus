```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This code implements a function that filters an input list of strings, returns a new list containing only those strings that have the specified prefix. The function uses the string starting search, which means that it checks if each string starts with the specified prefix, and if it does, it returns that string.