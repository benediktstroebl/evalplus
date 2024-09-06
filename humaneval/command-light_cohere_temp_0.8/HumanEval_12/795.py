```python
from typing import List

def longest(strings: List[str]) -> str:
    """ Returns the length of the longest string.
    """
    return max(len(s) for s in strings) or None
```
This function takes a list of strings as input and returns the length of the longest string in the list. It does this by using the max function and comparing the length of each string in the list with the current maximum length.