Here is a Python script that contains a self-contained function that filters an input list of strings for those that start with a given prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This function uses the startsswith operator to filter the strings in the list. The function returns a list of strings that start with the given prefix.