```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list, or None if the list is empty.
    """
    if not strings:  # Check if the list is empty
        return None

    longest_str = strings[0]  # Initialize the longest string with the first string in the list

    for string in strings[1:]:  # Iterate over the rest of the list
        if len(string) > len(longest_str):  # Check if the current string is longer
            longest_str = string  # Update the longest string

    return longest_str


# Test cases
print(longest([]))  # Expected output: None
print(longest(['a', 'b', 'c']))  # Expected output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Expected output: 'ccc'
```

This script defines the `longest` function as specified, with a clear docstring that explains its behavior. It then includes test cases to demonstrate its usage. The function uses a simple iterative approach to find the longest string in the list, returning the first one in case of a tie. If the input list is empty, it returns `None`.