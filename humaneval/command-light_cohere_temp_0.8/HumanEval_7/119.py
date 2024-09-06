```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [s for s in strings if s.contains(substring)]
```

This code defines a function **filter_by_substring** that filters a list of strings for a given substring. The function uses a **in-place filtering**, which means it creates a new list with all elements that contain the given substring.