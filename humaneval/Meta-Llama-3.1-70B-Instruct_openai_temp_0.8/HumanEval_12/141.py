```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list or None if the list is empty.
    """
    if not strings:  # Check if the list is empty
        return None
    return max(strings, key=len)  # Use built-in max function with key=len to find the longest string

# Test cases
print(longest([]))  # Expected output: None
print(longest(['a', 'b', 'c']))  # Expected output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Expected output: 'ccc'
```

This script defines the `longest` function as specified, including type hints and a docstring. The function uses the built-in `max` function with the `key=len` argument to find the longest string in the list. If the list is empty, the function returns `None`. The script also includes test cases to verify the function's behavior.