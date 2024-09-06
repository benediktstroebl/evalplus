```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Returns the longest string in the list.
    Args: strings (list of strings) 
    Returns: list of strings, the longest one.
    """
    return [max(strings, key=len)
```