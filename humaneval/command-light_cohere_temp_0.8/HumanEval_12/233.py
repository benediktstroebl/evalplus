```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Return the longest string in the list.
    Args:
        strings (List[str]): list of strings

    Returns:
        str: longest string
    """
    return max(strings, key=len)
```