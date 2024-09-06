```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings: list of strings
        prefix: str

    Returns:
        list of strings with the given prefix
    """
    return [s for s in strings if s.startswith(prefix)]
```

This Python script defines a function called `filter_by_prefix` that filters a list of strings based on whether their prefixes match a given prefix.  It returns a same list of strings that start with the given prefix.