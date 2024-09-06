Certainly, here's a Python script that defines a function `filter_by_prefix`, which filters a list of strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings: list of strings
        prefix: str

    Returns:
        list of strings that start with the given prefix
    """
    return [s for s in strings if s.startswith(prefix)]
```

This function takes a list of strings and a prefix as arguments. It returns a filtered list, which contains only the strings from the input list that start with the given prefix. 

It uses the list comprehension technique along with the `startswith` method from Python's string module.