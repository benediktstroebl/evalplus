```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    return [string for string in strings if string.startswith(prefix)]
```
This Python function filters a list of strings based on whether they start with a given prefix. It uses the Python's list comprehension to create a new list containing only the strings that match the condition. The function is designed to accept lists of strings and strings as its parameters, and the condition to filter by is specified as a string starting with the given prefix.