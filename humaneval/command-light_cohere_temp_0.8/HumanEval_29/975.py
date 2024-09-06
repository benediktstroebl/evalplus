```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function **filter_by_prefix** that takes in a list of strings and a prefix, and returns a new list that contains only the strings that start with that given prefix. The function uses the particular list comprehension to achieve this.