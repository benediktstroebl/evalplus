Here is a self-contained Python script with a function that filters Markdown code blocks based on their prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
The function uses the `startswith` method to filter the strings and returns a new list with the values that start with the given prefix.