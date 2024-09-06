```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function uses a list of strings and a prefix as input. It returns a strings from the list that start with the given prefix.