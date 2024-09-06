Here's the solution:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This function filters an input list of strings, accepting only those that start with a given prefix. It's tested by passing a test case, which includes an empty list and a list with various strings, some of which start with the specified prefix.