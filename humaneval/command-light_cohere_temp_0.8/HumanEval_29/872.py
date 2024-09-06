```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This Python function, `filter_by_prefix`, takes a list of strings and a prefix as input. It then returns a filtered list of strings that start with the given prefix. The function works by using a generator expression, which creates a list of strings from the input list. 

It checks if each string in the input list starts with the given prefix using the `startswith` method. If a condition is met, the string is added to the result list.