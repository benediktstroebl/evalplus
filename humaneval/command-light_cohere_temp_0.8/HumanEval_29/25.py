Here's the solution:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

The function uses a list comprehension to filter the input strings based on whether their prefix matches the given prefix. This approach is consistent and efficient for the problem.