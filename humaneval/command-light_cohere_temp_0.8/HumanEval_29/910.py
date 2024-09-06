```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): List of strings
        prefix (str): String to match as the prefix

    Returns:
        List[str]: List of strings with the given prefix
    """
    return [x for x in strings if x.startswith(prefix)]
```