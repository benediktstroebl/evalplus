```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function uses the starts-with operator to filter a list of strings, only keeping those that start with the given prefix. It is a concise and efficient way to achieve this problem's solution.