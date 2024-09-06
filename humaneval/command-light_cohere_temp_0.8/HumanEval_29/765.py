Here is a self-contained Python script that defines a function `filter_by_prefix` that filters an input list of strings based on their prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
The function uses the `startswith` method of the string to filter the strings in the list that start with the specified `prefix`.