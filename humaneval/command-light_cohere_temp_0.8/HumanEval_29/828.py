```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings for elements starting with a given prefix.
    Returns a list of strings with the given prefix as their start.

    Parameters:
        strings: list of strings
        prefix: string to search for
    """
    return [s for s in strings if s.startswith(prefix)]
```