Here's a Python script that defines a function `filter_by_prefix` solving the problem you described. 

```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings: list of strings
        prefix: string to match the prefix

    Returns:
        filtered_strings: list of strings that start with the given prefix
    """
    return [string for string in strings if string.startswith(prefix)]
```

This function uses a list comprehension to filter the input list, checking if each string starts with the provided `prefix`.