Here's a self-contained Python function that filters an input list of strings based on their prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This function uses the `startswith` method to filter the strings in the input list. It returns a particular string that starts with the specified prefix.