```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This Python function uses the startsswith operator to filter an input list of strings and returns a new list containing only the strings that start with the given prefix.