Here's a self-contained Python function that filters an input list of strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings by their prefix.

    Args:
        strings: List of strings
        prefix: The prefix to filter for

    Returns:
        List of strings that start with the given prefix
    """
    return [x for x in strings if x.startswith(prefix)]
```
This function, `filter_by_prefix`, takes a list of strings and a prefix as input. It returns a useful output by filtering out all the strings in the input list that start with the given prefix.