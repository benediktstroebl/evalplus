```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This Python function, `filter_by_prefix`, takes a list of strings and a prefix as input and returns a new list containing only the strings that start with that prefix. It uses the list comprehension to filter out the desired strings.