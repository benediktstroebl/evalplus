```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings: list of strings
        prefix: string to match as the prefix

    Returns:
        list of strings that start with the given prefix
    """
    return [string for string in strings if string.startswith(prefix)]
```

The provided Python script defines a function `filter_by_prefix` that takes two arguments: a list of strings `strings` and a string `prefix`. It returns a new list containing strings from the input list that start with the provided `prefix`. The function uses the `startswith` method of the string class to check if each string in the input list starts with the given `prefix`.