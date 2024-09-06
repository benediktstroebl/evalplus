Here's a self-contained Python function that filters an input list of strings based on a given prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```
The function uses a list comprehension to iterate over each string in the input list. The condition checks if the string starts with the given prefix using the `startswith()` method. The resulting list will strings that match the condition.