Here is a Python script that includes a self-contained function that solves the problem of finding the longest string in a list of strings:
```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Return the longest string in the list.
    >>> return longest(["a", "b" , "bb", "ccc"])
    'ccc'
    """
    return max(strings, key=len)
```
This script defines a function called longest that takes in a list of strings as input and returns the longest string in that list. The function uses the key=len method of the max function to return the longest string, and the max function is called with the list of strings and the length of the string as the key.