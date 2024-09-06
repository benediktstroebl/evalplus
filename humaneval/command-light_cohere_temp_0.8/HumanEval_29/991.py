Here's a self-contained Python script that implements the provided function `filter_by_prefix` that filters an input list of strings based on a given prefix:
```python
from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a') == []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    """
    return [string for string in strings if string.startswith(prefix)]
```

This script provides a complete function with tests and demonstrates how to use the function with different inputs.