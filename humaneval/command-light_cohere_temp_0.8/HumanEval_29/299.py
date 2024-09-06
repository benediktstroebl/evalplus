```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This code defines a function, `filter_by_prefix`, that takes in a list of strings and a prefix as arguments. The function returns a strings in the list that start with the provided prefix.