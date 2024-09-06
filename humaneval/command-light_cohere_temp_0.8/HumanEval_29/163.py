```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This function uses the Python list comprehension and the startsWith method to filter out the strings that start with a given prefix.