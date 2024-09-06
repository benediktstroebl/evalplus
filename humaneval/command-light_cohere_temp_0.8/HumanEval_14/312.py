```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[:string.find(char)] for char in string]
```