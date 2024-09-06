```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Return the longest string in a list.
    """
    list must not be empty
    return str(max(strings, key=len))
```
This function takes a list of strings as input and returns the longest string in the list. It does this using the using the max function with the key argument set to len, which returns the length of the string.