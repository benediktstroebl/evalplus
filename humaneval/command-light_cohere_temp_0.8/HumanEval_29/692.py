```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
The function uses the `startswith` method to check if each element in the strings list starts with the given `prefix`. The function returns a new list containing only the strings that match the condition.