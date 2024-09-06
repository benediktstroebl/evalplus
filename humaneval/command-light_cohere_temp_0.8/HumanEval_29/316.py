```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This code defines a function called **filter_by_prefix** that filters an input list of strings to only include those that start with a given prefix.  It returns a filter for that list of strings.