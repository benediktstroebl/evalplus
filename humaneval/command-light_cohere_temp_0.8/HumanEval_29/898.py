```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function accepts a list of strings and a prefix parameter, and it uses a list comprehension to filter the strings based on whether the string starts with the given prefix.