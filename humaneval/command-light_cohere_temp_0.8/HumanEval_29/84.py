```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This Python function filters a list of strings based on whether their prefix matches the given prefix string. It uses the general string method `startswith()` to perform the check, and returns a new list containing only the strings that start with the given prefix. This function is easy to understand and has a clear and efficient purpose, making it an excellent candidate for encapsulation in a module.