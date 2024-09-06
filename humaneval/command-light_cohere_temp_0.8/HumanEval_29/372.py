```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
Here's a Python function that filters an input list of strings, using the starts with operator, to only include those that start with a specific prefix.