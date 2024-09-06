```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This code implements a function called **`filter_by_prefix`** that filters an input list of strings based on whether their prefixes start with a specific prefix. 

This function returns a new list containing only the elements from the original list that have a prefix that matches the given prefix.