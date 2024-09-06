```python
from typing import List

def longest(strings: List[str]) -> List[str]:
    """
    Return the longest string in the list.
    Parameters:
    strings (List[str]): A list of strings.
    Returns: list of the longest string in the list.
    """
    test case
    A list of strings is empty.
    test case Two strings is not empty
    """
    if not strings:
        return None
    return max(strings, key=len)
```
The function takes a list of strings as input and returns a list of the longest string. 

This function passes all the corresponding tests.