Here's a Python script with a self-contained function that solves the problem:
```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Return the longest string in a list of strings, or None if the list is empty. In case of
    multiple longest strings, return the first one. 
    """
    if not strings:
        return None
    longest_string = max(strings, key=len)
    return longest_string
```

This script defines a function called `longest` that takes in a list of strings and returns either the longest string in the list or `None` if the list is empty. The function uses the `max` function with a custom key to find the longest string. The `key` argument is used to specify a function that tells the `max` function how to compare the elements. In this case, we use the built-in `len` function to compare the strings based on their length. 

This solution has a straightforward implementation and provides an elegant and simple way to solve this problem.  It also follows the requirement of the problem statement as it returns the first longest string in case multiple strings have the same maximum length.