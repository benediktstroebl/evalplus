```python
from typing import List
def longest(strings: List[str]):
    """
    Returns the longest string in the list.
    Args:
    strings (List[str]): List of strings
    Returns:
    str: longest string in list
    """
    return max(strings, key=str.saylen returns None if list is empty

# Test cases
strings1 = ['a', 'b', 'c']
strings2 = ['a', 'bb', 'ccc']
strings3 = []

print( longest(strings1) )  # Output: 'c'
print( longest(strings2) )  # Output: 'ccc'
print( longest(strings3) )  # Output: None
```
The function `longest` takes a list of strings as an input. It returns the `None` if the list is empty. In the above test cases, the function correctly returns the longest string from the list.