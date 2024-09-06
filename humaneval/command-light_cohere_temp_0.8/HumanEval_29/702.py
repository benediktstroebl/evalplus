```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function uses a generator expression to filter out the strings that start with the given prefix. It's a a concise and readable implementation, which eliminates the need for an additional list comprehension.