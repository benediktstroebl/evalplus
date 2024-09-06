```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [prefix for prefix in string.groupby(string, key=len)]
```
Do you need help with anything else with Python programming or code related topics?