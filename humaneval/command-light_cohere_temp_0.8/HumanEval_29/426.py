Here's a self-contained Python function that filters a list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
The function uses the startsswith operator to check if each string in the list starts with the given prefix. It returns a string.