Here is a Python script with a self-contained function that filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script defines a function called `filter_by_prefix` that takes a list of strings and a prefix as input. It uses the Python's list comprehension to filter the list of strings, only keeping the ones that start with the given prefix. The function returns a list of the filtered strings.

You can use this function to solve the problem and pass the corresponding tests.