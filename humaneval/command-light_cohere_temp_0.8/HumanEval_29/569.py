```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
The function returns a list of strings from the input list that starts with the given prefix. 

The function uses the typing module to ensure type safety and avoid any type-related errors.