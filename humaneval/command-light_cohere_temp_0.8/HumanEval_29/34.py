```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

The function uses a list comprehension with a filter function to achieve this. The function returns a list of strings that start with the given prefix.