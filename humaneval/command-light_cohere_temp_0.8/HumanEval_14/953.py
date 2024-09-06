```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.rep() if prefix != '' and not prefix.return longest_prefix = max(string, key=len)
    return [prefix for prefix in string if len(prefix) > longest_prefix]
```