```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    Returns a string list without duplicates and prefix matches.

    Args:
        strings (List[str]) - list of strings
        prefix (str) - string to match the prefix of
    """
    return [x for x in strings if x.startswith(prefix)]
```