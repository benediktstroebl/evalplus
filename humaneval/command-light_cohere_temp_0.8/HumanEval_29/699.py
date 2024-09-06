```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.

    Parameters:
        strings: List of strings. strings to filter. strings list of minimum characters string starting the next to prefix, starting at the first character.

    Returns:
        list of strings that start with the given prefix.

    Test:
    It should return the list of strings starting with 'cde', and nothing else.
    """
    example:
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]
```
Do you require additional assistance with code implementation or have other questions related to programming or AI models?