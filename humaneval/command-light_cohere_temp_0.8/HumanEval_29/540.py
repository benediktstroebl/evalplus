```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This Python function filters a list of strings based on a given prefix. It utilizes the filtering by checking if each element in the input string starts with the provided prefix, returning the matching elements.