Here's a self-contained Python function that filters strings based on a given prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
The function uses the `startswith` method to filter the strings in the list that start with the specified prefix. The return value is a list of strings that pass the filter.