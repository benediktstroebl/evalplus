Here is a Python script that contains a self-contained function that solves the problem of finding the longest string in a list of strings:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string from the list.
    """
    strings = [string.strip for string in strings]
    return strings[-1] if len(strings) > 0 else None
```