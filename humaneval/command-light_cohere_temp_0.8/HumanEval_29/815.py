```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings (List[str]): list of strings
        prefix (str): prefix string to search for

    Returns:
        List[str]: list of strings with matching prefixes
    """
    return [x for x in strings if x.startswith(prefix)]
```