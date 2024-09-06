Here is a self-contained Python script with a function that filters an input list of strings based on their prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
The filter_by_prefix function uses a list comprehension to filter the input list of strings based on whether they start with the given prefix.