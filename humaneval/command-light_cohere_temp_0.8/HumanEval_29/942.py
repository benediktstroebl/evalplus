```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings: list of strings
        prefix: string that must start the string

    Returns:
        list of strings that start with the given prefix
    """
    return [string for string in strings if string.startswith(prefix)]
```
This Python code defines a function called `filter_by_prefix`, which takes two arguments: a list of strings (`strings`) and a prefix string (`prefix`). The function returns a new list that contains only the elements of `strings` that have a prefix equal to `prefix`. The function is designed to efficiently filter and transform the input strings based on a given prefix, providing a practical solution for this common problem in Python programming.