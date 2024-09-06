Certainly! Here's a self-contained Python script with a function that filters an input list of strings based on a given prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix """
    return [x for x in strings if x.startswith(prefix)]
```

This script provides a function `filter_by_prefix` that filters an input list of strings based on a given prefix. The function returns a filtered list of strings that start with the given prefix.