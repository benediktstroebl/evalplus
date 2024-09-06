```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix
    Returns: list of strings that start with the given prefix
    """
    return [x for x in strings if x.startswith(prefix)]
```

This function is designed to filter and return a list of strings that start with a given prefix. The function utilizes the String type hint to enforce the expected data types for the parameter list and prefix.