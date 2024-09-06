```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function called `filter_by_prefix` that takes a list of strings and a prefix as input. The function returns a filtered list of strings that start with the given prefix. The function uses the filtering technique to achieve this, where it creates a new list by using the `startswith` method of the string object and then applies it to the list of strings. 

The function is a self-contained solution to the provided problem.