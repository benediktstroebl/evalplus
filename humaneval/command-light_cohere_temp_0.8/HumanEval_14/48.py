```python
from typing import List
def all_prefixes(string: str) -> List[str]:
    return [ prefix for prefix in string.a.lower() for string[:] ][:len(string):]
```
This function will return all prefixes of a given string, sorted from shortest to longest.