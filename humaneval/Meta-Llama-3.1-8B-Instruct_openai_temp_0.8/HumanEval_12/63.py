```python
from typing import List, Optional
from functools import reduce

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list or None if the list is empty.
    """
    
    # Check if the list is empty
    if not strings:
        return None
    
    # Use reduce to find the longest string
    return reduce(lambda x, y: x if len(x) >= len(y) else y, strings)

# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This script defines a function `longest` that takes a list of strings and returns the longest string. It uses the `reduce` function from the `functools` module to find the longest string by comparing all strings in the list. If the list is empty, it returns `None`. The test cases at the end demonstrate the function's behavior.