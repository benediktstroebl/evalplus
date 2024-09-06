```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ['a', 'ab', string[:1]] + [prefix[1:] if len(prefix) > 1 else prefix for prefix in string.string()]
```