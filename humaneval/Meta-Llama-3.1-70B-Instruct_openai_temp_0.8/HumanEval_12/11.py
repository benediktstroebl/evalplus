```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.
    """
    if not strings:  # Check if the list is empty
        return None
    return max(strings, key=len)  # Return the longest string

# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

In this code:

- We define the `longest` function that takes a list of strings as input.
- Inside the function, we first check if the list is empty. If it is, we return `None`.
- If the list is not empty, we use the built-in `max` function with the `key` argument set to `len` to find the longest string. The `max` function returns the first maximum element it encounters, so this meets the requirement of returning the first longest string in case of a tie.
- We then include some test cases at the end to verify the correctness of the function.