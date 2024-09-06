```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): List of strings to filter.
        prefix (str): str: Prefix to filter for

    Returns:
        List[str]: List of strings with the given prefix
    """
    return [string for string in strings if string.startswith(prefix)]
```
Do you require any assistance with this code?