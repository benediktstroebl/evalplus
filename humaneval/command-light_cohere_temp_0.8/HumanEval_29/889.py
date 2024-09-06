```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): List of strings.
        prefix (str): str

    Returns:
        List of strings that start with the given prefix
    """
    return [string for string in strings if string.startswith(prefix)]
```

This Python script defines a function `filter_by_prefix` that takes a list of strings and a prefix as arguments, and returns a new list of strings that start with the given prefix.