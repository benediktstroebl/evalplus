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
    return max(strings, key=len)  # Return the longest string

# Test cases
print(longest([]))  # Should print: None
print(longest(['a', 'b', 'c']))  # Should print: 'a'
print(longest(['a', 'bb', 'ccc']))  # Should print: 'ccc'
```

This script defines a function `longest` that takes a list of strings as input. It checks if the list is empty, and if so, returns `None`. Otherwise, it uses the `max` function with the `key=len` argument to find the longest string in the list and returns it. The `key` argument tells `max` to use the length of each string as the comparison key, so it returns the longest string. 

In the test cases, we call the `longest` function with different inputs and print the results to verify that it behaves as expected.