Certainly! Here's the Python code with a self-contained function that filters an input list of strings based on their prefix:

```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [x for x in strings if x.startswith(prefix)]
```

This function uses the `startswith` method to check if each string in the input list starts with the given `prefix`. It returns a new list containing only those strings.