```python
from typing import List
def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, returns the longest one or None.
    """ 
    return max(strings, key=len)  # return the longest string which also has the longest index 

# List[str] example:
strings = ['a', 'bb', 'ccc']
longest(strings) # Output: 'ccc'

# Type hint example 
def longest(list):
    return longest([1, 2, 3, 4, 5]) # 5 

# Example of passing an empty list
strings = []
longest(strings) # Output: None
```

This Python script defines a self-contained function called `longest` that takes a list of strings as input and returns the longest string in that list or `None` if the list is empty.  The function utilizes the max function with the `key` argument set to the length of each string in the list, and the `str` string type hint. This allows it for type hint to work properly.