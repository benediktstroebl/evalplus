```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
The function takes a list of strings and a prefix as parameters, then returns a new list containing only the strings that start with the given prefix.