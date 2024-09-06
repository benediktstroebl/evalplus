```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This Python code implements a function `filter_by_prefix` that filters an input list of strings, returning a new list containing only the elements that begin with a specified prefix. The function utilizes the particular string `startswith` method to achieve this.