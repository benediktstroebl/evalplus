```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    : Returns a examples:
        - Only include strings that start with the given prefix.
        - This will list of filtered strings.

    Args:
    strings: List of strings to filter
    prefix: The prefix string to search for
    """
    return [string for string in strings if string.startswith(prefix)]
```