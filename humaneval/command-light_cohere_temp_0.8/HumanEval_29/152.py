Here's the Python script with a self-contained function that filters an input list of strings based on their prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list containing only the strings from the input list that start with the given prefix. 

This function effectively filters out strings that do not have the specified prefix at the beginning.