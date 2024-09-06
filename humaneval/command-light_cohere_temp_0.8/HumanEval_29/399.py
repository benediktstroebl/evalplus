```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function utilizes the `startswith` method to check if each element in the input list starts with the given prefix. It then returns a list of matching strings.