```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that takes in a list of strings and a prefix as arguments. It uses the filtering with the list comprehension to only return strings that start with the given prefix. 

This code is a good implementation of the problem, and it can be easily understood and modified.