Here's a self-contained Python function that filters a list of strings based on a given substring:
```python
from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    return [x for x in strings if x.contains(substring)]
```

This function uses the contains() method to check if each string in the list contains the given substring. It then returns a