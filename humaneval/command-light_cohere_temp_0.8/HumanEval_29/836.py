The Python script has a self-contained function that filters strings based on their prefixes:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```

This function creates an empty list and then iterates over the input list of strings. It uses the `startswith` method to check if each string starts with the given prefix. The function returns a list of matching strings.