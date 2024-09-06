Here's the improved Python script that provides a self-contained function and passes the test cases:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix."""
    return [string for string in strings if string.startswith(prefix)]
```

This function efficiently filters a list of strings based on their prefix, returning only the desired strings.