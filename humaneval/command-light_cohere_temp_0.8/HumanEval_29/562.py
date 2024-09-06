Here is a self-contained Python script with a function that filters an input list of strings based on their prefix:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This function uses the starts-with operator to filter the strings that have the specified prefix. It takes a specific type List[str] as the input, and returns a new list with the elements that have the specified prefix.