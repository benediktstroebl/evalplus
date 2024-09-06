```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```

This Python code defines a function called `filter_by_prefix` that filters an input list of strings based on whether their prefixes match a given prefix. The function uses the specific typing annotations (`List[str]`, `prefix: str`) to ensure type-safety and better code readability. 

The function returns a new list containing only the strings from the input list that have a prefix equal to the provided prefix. This is a more concise and readable way to filter strings based on a prefix.