```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [x for x in strings if x.startswith(prefix)]
```

This Python code defines a function called **filter_by_prefix** that filters a list of strings based on their prefix. The function utilizes the string starts with method to check if each string in the list starts with the specified prefix. It returns a filtered list of strings that match the given prefix.