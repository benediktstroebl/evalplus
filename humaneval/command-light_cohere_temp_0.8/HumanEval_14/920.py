```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [c for c in string if c.isalpha()]
```
all_prefixes('abc').should be ['a', 'ab', 'abc']
```