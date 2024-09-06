Here is a self-contained Python script that includes the function filter_by_prefix, which is used to solve the problem you described:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    :strings: List of strings to filter
    :prefix: Prefix to filter for

    Returns: List of strings that start with the given prefix
    """
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings and a prefix as input, and returns a new list that contains only the strings that start with the given prefix. It uses the process to iterate through the input list and apply the condition to filter the strings.