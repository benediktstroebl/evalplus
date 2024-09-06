Here's the solution:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This function uses a list comprehension to filter the input list of strings based on whether their prefix matches the given prefix.