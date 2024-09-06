Here's the solution for the markdown code block problem:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a') --> []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') --> ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]
```

The function uses a generator expression to iterate over each string in the list, and checks if the string starts with the given prefix. It returns a simple strings that start with the given prefix.