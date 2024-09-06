Here's a self-contained Python script with a function that filters an input list of strings for a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings and return those starting with a given prefix.

    Args:
        strings: List of strings.
        prefix: str
    """
    Returns:
        List of strings starting with the given prefix
    """
    return [s for s in strings if s.startswith(prefix)]
```