Here's the solution:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [s for s in strings if s.startswith(prefix)]
```
This Python code defines a function `filter_by_prefix` that filters an input list of strings based on a given prefix. The function uses the `startswith` method to check if each string in the list starts with the given prefix. It returns a list of all the strings from the list that start with the specified prefix. 

This solution is self-contained within the Python language and does not require any external libraries or modules.