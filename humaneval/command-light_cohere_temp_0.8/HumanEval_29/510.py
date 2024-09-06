```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This script defines a function **filter_by_prefix** that filters an input list of strings based on a given prefix. 

The function uses the **startswith** method to check if each element in the strings list starts with the given prefix.