Here is a Python script that includes a self-contained function to solve the problem of filtering strings that start with a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    Args:
    strings: list of strings
    prefix: string that must start the string to be included in the filtered list

    Returns:
    list: list of strings that start with the given prefix
    """
    return [string for string in strings if string.startswith(prefix)]
```

This script defines a function called `filter_by_prefix`, which takes a list of strings and a prefix as arguments. The function returns a filtered list of strings that start with the given prefix. The use of the list comprehension and a Python `startswith` function to achieve this.