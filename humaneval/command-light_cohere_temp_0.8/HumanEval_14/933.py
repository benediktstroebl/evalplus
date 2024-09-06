Here's the solution:
```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return ["".join([c for c in s if s.startswith(c) else c])
        for s in string.get_ascii_lowercase_strings()]
```
Do you need assistance with anything else?