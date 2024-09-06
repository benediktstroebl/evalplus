Here is a self-contained Python script that defines a function `filter_by_prefix` solving the problem you described:

```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes two arguments: a list of strings `strings` and a prefix `prefix`. It returns a new list containing only the strings from the input list that start with the specified prefix. 

This function effectively filters the list based on the given prefix.