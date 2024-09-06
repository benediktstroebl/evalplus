```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This script defines a function called **filter_by_prefix** that filters an input list of strings, removing those that do not start with a given prefix. It uses the typing to provide type hints for the function, which helps with better code readability and future compatibility. The function returns a list of the strings that start with the given prefix.