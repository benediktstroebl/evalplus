```python
from typing import List

def all_prefixes(string: str) -> List[str]:
    return [''.join(''.join(i). band) for string.range(string) for band in string for i in range(1, len(string)+1)]
```