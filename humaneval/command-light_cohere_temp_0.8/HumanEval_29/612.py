```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
The function uses the `startswith` method to filter out only the strings that start with the given `prefix`.