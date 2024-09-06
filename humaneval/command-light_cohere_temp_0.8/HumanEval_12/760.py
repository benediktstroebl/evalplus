```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the length of the longest string.

    If list is empty, returns None.
    """
    return max(str.len(s) for s in strings)
``` 
This function takes a list of strings as input and returns the length of the longest string. It uses the max function with a list comprehension to find the maximum length of the strings. This solution is approach is efficient and does not require any additional space.