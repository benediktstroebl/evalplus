```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.

    Args:
        strings (List[str]): A list of strings.

    Returns:
        Optional[str]: The longest string or None if the input list is empty.
    """

    # Check if the input list is empty
    if not strings:
        return None

    # Use the built-in max function with a custom key function to find the longest string
    # The key function is a lambda function that returns the length of each string
    # The max function will return the first string with the maximum length in case of multiple strings with the same length
    return max(strings, key=lambda s: len(s))

# Test cases
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This script defines a function `longest` that takes a list of strings as input and returns the longest string. If the input list is empty, it returns `None`. The function uses the built-in `max` function with a custom key function to find the longest string. The key function is a lambda function that returns the length of each string. The `max` function returns the first string with the maximum length in case of multiple strings with the same length. The script also includes test cases to demonstrate the function's behavior.