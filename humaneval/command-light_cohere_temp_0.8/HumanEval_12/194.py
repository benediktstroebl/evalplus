```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the longest string in the list.
    """
    return max(strings, key=len)

# Tests
strings = ['a', 'b', 'c']
longest(strings)  # Output: c
strings = ['aa', 'bb', 'ccc']
longest(strings)  # Output: c
strings = []
strings. longest 

# Output: None (empty list)
``` 
This script defines a function called `longest` that takes a list of strings and returns the longest string in the list. The `max` function is used to compare the lengths of the strings and return the longest one.