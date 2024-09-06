```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join[i for i in range(len(string) + 1) if string[i:].isalpha()]
```