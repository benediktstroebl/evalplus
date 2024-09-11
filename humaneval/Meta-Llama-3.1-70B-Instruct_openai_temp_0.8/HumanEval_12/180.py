```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list or None if the list is empty.
    """
    if not strings:
        # If the list is empty, return None
        return None

    # Use the max function with the key argument set to len to find the longest string
    # The max function returns the first item with the maximum value in case of a tie
    return max(strings, key=len)


# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This script defines the `longest` function as per the provided specification. It first checks if the input list is empty and returns `None` if so. Otherwise, it uses the built-in `max` function with the `key` argument set to `len` to find the longest string in the list. The `max` function returns the first item with the maximum value in case of a tie, which meets the requirement of returning the first longest string in case of multiple strings of the same length. The script also includes test cases to verify the function's behavior.