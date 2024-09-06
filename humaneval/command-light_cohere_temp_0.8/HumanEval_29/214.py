Here is a Python script with a self-contained function that solves the problem of filtering an input list of strings based on a prefix:
```python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings by prefix.

    Args:
        strings (List[str]): List of strings
        prefix (str): String prefix to filter for

    Returns:
        List[str]: List of strings that start with the given prefix
    """
    return [string for string in strings if string.startswith(prefix)]
```

This function uses a list comprehension to iterate over each string in the input list and checks if the string starts with the provided prefix. The function then returns a list of matching strings.