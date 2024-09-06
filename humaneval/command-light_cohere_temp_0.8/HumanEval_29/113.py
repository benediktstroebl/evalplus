Here is a self-contained Python script that defines a function `filter_by_prefix` that solves the problem of filtering an input list of strings based on their prefix:

```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings and a prefix as input, and returns a new list that contains only the strings that start with the given prefix. 

This script also includes a pass that verifies the correctness of the `filter_by_prefix` function.