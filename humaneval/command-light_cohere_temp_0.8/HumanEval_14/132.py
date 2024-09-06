```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [w for w in string if w.isalpha()]
```