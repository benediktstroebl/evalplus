Here's the Python script with a self-contained function that filters an input list of strings based on a given prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
The function filter_by_prefix uses the startswith operator to filter the strings in the list that start with the given prefix. The function returns a list of the matching strings.