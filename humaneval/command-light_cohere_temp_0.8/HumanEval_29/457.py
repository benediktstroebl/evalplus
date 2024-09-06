Here's a self-contained Python function that filters an input list of strings based on a given prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings by prefix.

    Args:
        strings (List[str]): list of strings to filter
        prefix (str): prefix to search for

    Returns:
        List[str]: list of strings that start with the given prefix
    """
    return [x for x in strings if x.startswith(prefix)]
```

The function takes a list of strings and a prefix as input and returns a new list containing only the strings from the input list that start with the specified prefix.