```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
The function filter_by_prefix takes a list of strings and a prefix as input, and returns a new list containing only the strings that start with the given prefix. It uses the `startswith` method from Python strings module to filter the strings.