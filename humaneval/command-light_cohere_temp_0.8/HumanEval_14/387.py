```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [i for i in string if i.isalpha()]
```