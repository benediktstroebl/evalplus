```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Out of list of strings, return the longest one.
    """
    return max(strings, key=len)
    """
    return [x for x in strings if len(x) == longest(strings, key=len)]
``` 
This function efficiently solves the problem by utilizing the `max()` function along with the `len` built-in function. 
The key argument of the `max()` function is set to `len`, which returns the length of the strings in the list.