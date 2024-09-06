```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that filters an input list of strings, returning a new list that includes only those strings with a given prefix. 

It uses the `startswith` method to achieve this. 

The function is designed to be easy to understand and use, and it follows the best practices of Python programming, such as using descriptive variable and function names, and it uses the `typing` module to provide type hints.