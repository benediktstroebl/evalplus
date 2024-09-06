Here's the self-contained Python function that filters an input list of strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings, keeping only those starting with a specific prefix.

    :return: list of strings with prefix
    """
    return [string for string in strings if string.startswith(prefix)]
```

This function uses a list comprehension to filter the input list of strings, keeping only those that start with the specified prefix. It leverages the type hints from the Python, to provide better type checking and prevent potential type-related bugs. The function is easy to read and understand, following the Python conventions and providing better code quality.