```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Return the longest string in the list.
    Args:
        strings (List[str]): List of strings.
    Returns: the first string that has the maximum length.
    """
    return None if the list is empty
    """
    if not strings:
        return None
    return max(strings, key=len)

# Tests
print(longest(['a', 'b', 'c']))    # Output: 'a'
print(longest(['aa', 'bb', 'ccc']))  # Output: 'ccc'
print(longest([]))         # Output: None
print(longest(['a', 'x', 'y']))  # Output: 'a'
``` 
The provided code has a function called **longest** that accepts a list of strings as input and outputs the longest string. The function has an built-in test to check the functionality of the **longest** function.