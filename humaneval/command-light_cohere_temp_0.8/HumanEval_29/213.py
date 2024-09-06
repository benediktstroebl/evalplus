```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings only for ones that start with a given prefix"""
    return [string for string in strings if string.startswith(prefix)]
```
The filter_by_prefix function uses a list of strings and a prefix to filter only the strings that start with the given prefix. The function returns a filtered list of strings.