Here's the self-contained Python script that implements the provided function definition:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This script defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. It uses the `startswith` method to compare each string in the list with the given prefix.