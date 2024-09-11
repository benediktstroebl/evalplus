```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string in the list or None if the list is empty.
    """
    # Check if the input list is empty
    if not strings:
        return None

    # Use the built-in max function with the key argument set to len to find the longest string
    # The max function returns the first item with the maximum value in case of a tie
    return max(strings, key=len)


# Test cases
print(longest([]))  # Expected output: None
print(longest(['a', 'b', 'c']))  # Expected output: 'a'
print(longest(['a', 'bb', 'ccc']))  # Expected output: 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string in the list. If the input list is empty, the function returns `None`. The function uses the built-in `max` function with the `key` argument set to `len` to find the longest string. The `max` function returns the first item with the maximum value in case of a tie.

The script also includes three test cases to verify the correctness of the `longest` function. The expected output of each test case is provided in a comment.