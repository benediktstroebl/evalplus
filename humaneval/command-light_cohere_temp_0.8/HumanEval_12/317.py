```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Out of list of strings, return the longest one.
    Args:
    strings (List[str]): A list of strings

    Returns:
    List of strings with the longest one.
    """
    return [max(strings, key=len)
    ```