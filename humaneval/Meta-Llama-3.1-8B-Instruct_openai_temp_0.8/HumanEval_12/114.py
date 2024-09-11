```python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """
    Out of list of strings, return the longest one. 
    Return the first one in case of multiple strings of the same length. 
    Return None in case the input list is empty.

    Args:
    strings (List[str]): A list of strings.

    Returns:
    Optional[str]: The longest string in the list, or None if the list is empty.
    """
    if not strings:  # Check if the list is empty
        return None

    return max(strings, key=len)  # Use the max function to find the longest string
```

You can test this function using the provided test cases:

```python
print(longest([]))  # None
print(longest(['a', 'b', 'c']))  # 'a'
print(longest(['a', 'bb', 'ccc']))  # 'ccc'
```

This script defines the `longest` function, which takes a list of strings as input and returns the longest string. It first checks if the input list is empty, and if so, returns `None`. Otherwise, it uses the `max` function with the `key=len` argument to find the longest string in the list. The test cases at the end demonstrate the function's behavior.