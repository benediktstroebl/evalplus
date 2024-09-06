```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This Python script defines a function called `filter_by_prefix` that filters an input list of strings based on whether their prefixes match a given prefix. The function returns a filtered list of strings that start with the specified prefix. 

The function uses the "startswith" method to check the prefix match and returns the desired filtered list.