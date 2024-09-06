```python
import re
from typing import List

def all_prefixes(string: str) -> List[str]:
    # Find all non-empty prefixes of the input string and sort them in ascending order
    return sorted(re.findall(r'^(\w+)', string), key=lambda x: len(x), reverse=True)
```