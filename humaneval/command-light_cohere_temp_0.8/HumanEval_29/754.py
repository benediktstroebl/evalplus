```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This Python script defines a function `filter_by_prefix` that filters a list of strings based on whether the string starts with a specific prefix. It uses the filtered list comprehension to create a new list containing only the strings from the input list that start with the given prefix.