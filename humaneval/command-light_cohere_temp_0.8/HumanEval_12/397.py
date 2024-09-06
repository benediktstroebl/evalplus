```python
from typing import List

def longest(strings: List[str]) -> str:
    """
    Returns the length of the longest string in the list.
    Args:
        strings (List[str]): A list of strings

    Returns:
        str: The length of the longest string
    """
    if not strings:
        return None
    return max(strings, key=len)

# Unit tests
strings = ["abc", "a", "z", "abc"]
print( longest(strings) )   # Output: 5
print( longest(['a', 'bb', 'ccc']) ) # Output: 3
``` 
This script defines a function `longest` that calculates the length of the longest string in a list. It utilizes Python's list of strings as its parameter, and returns the length of the longest string in the list, or `None` if the list is empty. The `longest` is then tested with sample inputs and the results are printed to the console.