Here is a Python script that contains a self-contained function that filters an input list of strings based on a prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This script provides a function that filters an input list of strings based on a given prefix. The function uses the Python's `startswith` method to check if each string starts with the given prefix. It returns a `List[string]` for each string that starts with the given prefix from the input list.