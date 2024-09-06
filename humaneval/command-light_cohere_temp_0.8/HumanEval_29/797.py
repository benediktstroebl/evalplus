Here is a self-contained Python script that implements the filter_by_prefix function, which filters an input list of strings based on their prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This script provides a function that takes a list of strings and a prefix, and returns a new list that contains only the strings from the input list that start with the given prefix. The function uses the Python's built-in `startswith` method to efficiently filter the strings.

This function is self-contained and provides a solution to the problem statement you provided.