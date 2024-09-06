```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This function filters an input list of strings and returns a new list that contains only the strings that start with the specified prefix. It utilizes the filtering using a list comprehension with a generator expression, and the if statement checks if the current string starts with the given prefix.