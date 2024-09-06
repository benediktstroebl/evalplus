```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Return the longest string in the list.
    Args:
        strings (List[str]): list of strings.
    Returns: a list of strings, returns a list of the longest string.
    """
    return [max(strings, key=len, return_list=True)
``` 
This solution is a self-contained Python function that takes a list of strings as input and returns the longest string in the list.