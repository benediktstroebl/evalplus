```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
The function uses a generator expression to filter out strings that start with the given prefix. The function then returns a list of these filtered strings.