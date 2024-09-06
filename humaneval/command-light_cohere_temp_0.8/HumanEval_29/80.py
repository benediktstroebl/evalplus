```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This Python function, `filter_by_prefix`, takes a list of strings and a prefix as arguments. It then iterates over each string in the list, and returns a new list containing only those strings that start with the specified prefix. The function utilizes the specific type hints (from the `typing` module) to enforce type-checking and improve code readability.