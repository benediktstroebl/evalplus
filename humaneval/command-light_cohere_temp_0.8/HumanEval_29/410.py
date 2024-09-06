```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This code implements a function **`filter_by_prefix`** that takes a list of strings and a prefix as input. It uses the recommended Python list comprehension to filter the list of strings and return only the ones that start with the given prefix.