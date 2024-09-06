```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
The provided Python script defines a function `filter_by_prefix` that filters an input list of strings based on whether their prefixes match a given prefix. 

The function uses the `startswith` method to check if each string in the list starts with the specified prefix.

The function returns a new list containing only the strings from the original list that match the given prefix.