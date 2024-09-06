Here is a Python script that includes a self-contained function that filters an input list of strings based on their prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This function uses the `startswith` method to filter the strings in the list that start with the given prefix.