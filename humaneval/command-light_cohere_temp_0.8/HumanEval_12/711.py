```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the length of the longest string in the list.
    """
    list must contain only strings. 
    If list must not be empty. 
    """
    longest([]) raises an error 
    """
    if not strings:
        raise ValueError("Input list cannot be empty")
    return max(strings, default='')
```
The function longest takes a list of strings as input and returns the length of the longest string in the list. The function first checks if the list is empty, and if so, it raises a ValueError.