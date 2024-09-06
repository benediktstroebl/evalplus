```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    : Parameters:
        strings (List[str]) - List of strings to filter.
        prefix (str) - str - Prefix to search for

    Returns:
        List of strings that start with the given prefix
    """
    return [string for string in strings if string.startswith(prefix)]
```
This script defines a function **filter_by_prefix** that filters an input list of strings, ensuring that only those starting with a specified prefix are returned in the output.