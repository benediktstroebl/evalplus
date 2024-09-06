```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [p for p in string if p.isalpha()]
```