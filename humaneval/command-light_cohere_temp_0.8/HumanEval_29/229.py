Here's the solution:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
This function uses the `startswith` method to filter out strings from the input list that start with the given `prefix`. The output is a new list that contains only those matching strings.