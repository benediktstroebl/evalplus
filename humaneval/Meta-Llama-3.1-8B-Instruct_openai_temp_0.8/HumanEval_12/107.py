```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
    strings (List[str]): A list of strings

    Returns:
    Optional[str]: The longest string in the list or None if the list is empty
    """
    if not strings:
        return None
    return max(strings, key=len)

# Test cases
print(longest([]))  # Expected: None

print(longest(['a', 'b', 'c']))  # Expected: 'a'
print(longest(['a', 'bb', 'ccc']))  # Expected: 'ccc'
```

This Python script defines a function `longest(strings)` that takes a list of strings as input and returns the longest string. If multiple strings have the same maximum length, it returns the first one. If the input list is empty, it returns `None`. The script also includes test cases to demonstrate the function's behavior.