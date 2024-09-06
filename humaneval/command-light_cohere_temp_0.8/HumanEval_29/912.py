```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This Python code defines a function called `filter_by_prefix` that takes a list of strings and a prefix as input. It then creates a filtered list containing only the strings that start with the given prefix using the `startswith` method. 

This function can be used to efficiently filter and transform data with a specific prefix.