Here is a Python script that includes a self-contained function that filters an input list of strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This function uses a list of strings and a prefix parameter to filter the strings in the list. It uses the `startswith` method from Python's string module to check if each string starts with the given prefix.