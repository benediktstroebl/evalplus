Here's a Python script that contains a self-contained function `longest()` that accepts a list of strings and returns the longest string from the list:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the longest string in the list.
    """
    # List comprehension to find the longest string
    return max(strings, key=len)
```

This function utilizes the `typing` module to provide better type hints and better-coded error handling.