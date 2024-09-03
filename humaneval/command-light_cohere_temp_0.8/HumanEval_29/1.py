```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
The filter_by_prefix function filters an input list of strings, returning only those that start with a given prefix. The function uses the string.slist to pass, and returns a list of strings that start with the specified prefix. 

This is a self-contained solution and passes all tests.