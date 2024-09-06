Here's the solution:

```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function uses the `startswith` method to check if each string in the input list starts with the given `prefix`. It returns a new list containing only the strings that match this condition.