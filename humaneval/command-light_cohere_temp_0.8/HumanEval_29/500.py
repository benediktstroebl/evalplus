```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This Python function, `filter_by_prefix`, takes a list of strings and a prefix as input. It returns a filter the using the list, only keeping the elements of the input list that start with the given prefix.