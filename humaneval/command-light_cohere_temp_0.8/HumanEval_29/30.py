Here's a self-contained Python function that filters an input list of strings based on a given prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This function uses the Python in operator `in` to filter out strings from the input list that start with the specified prefix.