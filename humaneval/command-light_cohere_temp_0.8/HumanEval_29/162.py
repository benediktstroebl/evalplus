The Python script with the self-contained function and tests:
```python
from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    Returns: list of strings that start with the given prefix as output.

    Args:
        strings: list of strings
        prefix: str, the prefix to filter for

    Returns:
        List[str], list of strings that start with the given prefix
    """
    return [string for string in strings if string.startswith(prefix)]
```

This script defines a function `filter_by_prefix` that takes a list of strings and a prefix as input, and returns a new list of strings that start with the given prefix. The function uses the basic Python list comprehension with the `startswith` method to filter the strings in the list.