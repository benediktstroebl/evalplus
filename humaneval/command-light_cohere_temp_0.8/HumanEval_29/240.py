```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings only for ones that start with a given prefix."""
    return [x for x in strings if x.startswith(prefix)]
```

The provided Python script defines a function `filter_by_prefix` that filters an input list of strings, returning a new list containing only the elements that begin with a specific prefix. This is a way is achieved through using a list comprehension with a lambda function that checks if each element in the input list starts with the given prefix.