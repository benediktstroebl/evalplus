Here's the solution:

```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This function uses a list comprehension to filter out strings that start with the given `prefix`. The function takes a list of strings and a prefix as input, and returns a new list that contains only the strings that start with the given prefix.