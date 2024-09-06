```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This Python code defines a function named `filter_by_prefix` that takes two parameters: `List[str] strings` represents a list of strings, and `str prefix` is a string representing a prefix to filter. The function uses the Python's `list comprehension` to iterate through the strings in the input list. The function returns a strings in the list that start with the specified prefix.