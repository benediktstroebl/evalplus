```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This code implements a filter_by_prefix function that takes a list of strings and a prefix as input. It uses the filter syntax to filter the list of strings and only returns the ones that start with the given prefix. 

This code is well-contained and passes all the corresponding tests.