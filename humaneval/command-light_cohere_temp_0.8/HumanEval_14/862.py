```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.
    if not prefix.isalpha():
        strings = string.split()
    open('', del(string))
    if not any(char.isalpha() for char in string):
        return []
    return [prefix for prefix in strings if prefix.isalpha()]
```