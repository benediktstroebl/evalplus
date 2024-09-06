```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.str.split() if not starts as:
        if prefix not '':
            return []
        else:
            return [prefix] + all_prefixes(prefix + ' ')
    return []

def all_prefixes_test():
    return all(map(str.split, input()))
```