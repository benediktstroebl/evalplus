Here's a self-contained Python script that defines a function **`filter_by_prefix`** that filters an input list of strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [string for string in strings if string.startswith(prefix)]
```

This script provides a clear and concise function that meets the problem's requirements.