```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This script defines a function called `filter_by_prefix` that filters an input list of strings to only include those that start with a specific prefix. It utilizes the string matching and creates a new list with matching strings.